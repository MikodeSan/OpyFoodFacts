# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:14:16 2016

@author: doZan
"""

import sys
import os
import logging as lg

from PyQt5.QtCore import Qt, QItemSelection, QModelIndex, QDateTime
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QAbstractItemView #, QHeaderView, QTreeWidgetItem, QInputDialog

from ui_opynfacts import Ui_Form

# add 'model' package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# add 'database' interface package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database_json import ZDataBase_JSON as database


class ZOpynFacts_View(QWidget):

    PROJECT_NONE = "None"
    #    __CREDIT_TREE_DATA_LABEL = ['Label', 'Id.', 'Capital']

    def __init__(self, model, parent=None):

        super(ZOpynFacts_View, self).__init__(parent)

        self.__lg = lg
        self.__lg.basicConfig(level=lg.DEBUG)

        # Model
        self.__model = model

        # view data
        self.__selected_category_lst = []

        # Initialize main UI form
        self.__create_widgets()

        # set model for category view
        self.category_stdmodel = QStandardItemModel()
        self.ui.category_view.setModel(self.category_stdmodel)
        self.ui.category_view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # populate category view model
        self.__update_view_category()
        category_selection_model = self.ui.category_view.selectionModel()
        category_selection_model.selectionChanged[QItemSelection, QItemSelection].connect(self.__update_data_selected_categories)

        # set model for product view
        self.__product_mdl = QStandardItemModel()
        self.ui.product_view.setModel(self.__product_mdl)
        self.ui.product_view.setSelectionMode(QAbstractItemView.SingleSelection)

        # populate product view model
        product_data_lst = self.__model.products_from_categories([])        
        self.__update_view_product('product', product_data_lst)
        product_selection_model = self.ui.product_view.selectionModel()
        product_selection_model.selectionChanged[QItemSelection, QItemSelection].connect(self.__update_data_selected_product)

        self.ui.product_select_pbtn.clicked[bool].connect(self.__add_product_2_favorite)

        # set model for alternative product view
        self.__alternative_mdl = QStandardItemModel()
        self.ui.alternative_view.setModel(self.__alternative_mdl)
        self.ui.alternative_view.setSelectionMode(QAbstractItemView.SingleSelection)

        altern_category_cbox = self.ui.altern_category_cbox
        altern_category_cbox.currentIndexChanged[int].connect(self.__update_data_alternative_product)
        
        self.ui.alternative_select_pbtn.clicked[bool].connect(self.__add_alternative_2_favorite)

        # set model for alternative product view
        self.__favorite_stdmdl = QStandardItemModel()
        self.ui.favorite_view.setModel(self.__favorite_stdmdl)
        self.ui.favorite_view.setSelectionMode(QAbstractItemView.SingleSelection)

        # populate favorite view model
        product_data_lst = self.__model.products_from_categories([], is_favorite=True)        
        self.__update_view_product('favorite', product_data_lst)

        self.ui.favorite_remove_pbtn.clicked[bool].connect(self.__remove_favorite)

    def __create_widgets(self):

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def __update_view_category(self):

        # get category data
        category_data_lst = self.__model.categories()
        
        # view
        self.ui.category_view.setSortingEnabled(False)
        self.category_stdmodel.clear()
        self.category_stdmodel.setHorizontalHeaderLabels(['Category'])

        for data_dct in category_data_lst:

            item = QStandardItem( data_dct['name'] )
            item.setData(data_dct['id'])
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            self.category_stdmodel.appendRow(item)

        self.ui.category_view.setSortingEnabled(True)

    def __update_view_product(self, model_type, product_data_lst):

        # view
        is_checked = True

        if model_type == 'product':
            model = self.__product_mdl
        elif model_type == 'alternative':
            model = self.__alternative_mdl
        elif model_type == 'favorite':
            model = self.__favorite_stdmdl
        else:
            is_checked = False

        if is_checked:

            model.clear()

            header_lst = ['Brand', 'Name', 'code', 'Store', 'Nutri-Score', 'Nova score', 'UK Nutri-Score', 'Edited']
            model.setHorizontalHeaderLabels(header_lst)


            row_idx = 0
            for data_dct in product_data_lst:

                item_lst = []

                item = QStandardItem( data_dct['brands'] )
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item_lst.append(item)

                item = QStandardItem( data_dct['name'] )
                item.setData(data_dct['product_code'])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item_lst.append(item)

                item = QStandardItem( data_dct['product_code'] )
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item_lst.append(item)

                item = QStandardItem( ''.join(data_dct['stores']) )
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item_lst.append(item)

                grade = data_dct['nutrition_grades']
                if grade == 'z':
                    grade = ''
                item = QStandardItem( grade )
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item_lst.append(item)

                nova = data_dct['nova_group']
                # print(nova)
                if int(nova) < 127:
                    s = str(nova)
                else:
                    s = ''
                item = QStandardItem( s )
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item_lst.append(item)

                # nutrition_score = data_dct['nutrition_score']
                # if nutrition_score >= 0:
                #     s = str(nutrition_score)
                # else:
                #     s = ""
                # item = QStandardItem( s )
                # item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                # item_lst.append(item)

                # time = data_dct['last_modified_t']
                # if time >= 0:
                #     s = str(QDateTime().setTime_t(time))
                # else:
                #     s = ""
                # item = QStandardItem( s )
                # item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                # item_lst.append(item)

                model.appendRow(item_lst)
                # model.setItem(row_idx, item)
                row_idx = row_idx + 1

    def __update_data_selected_categories(self, selected_item, deselected_item):
        """ Get the list of selected category items, then get item data back and update the list of selected category id. """

        # deselected items
        for model_index in deselected_item.indexes():

            category_id = model_index.data(Qt.UserRole+1)
            
            if category_id in self.__selected_category_lst:
                self.__selected_category_lst.remove(category_id)

        # new selected items
        for model_index in selected_item.indexes():

            category_id = model_index.data(Qt.UserRole+1)
            
            if category_id not in self.__selected_category_lst:
                self.__selected_category_lst.append(category_id)
        
        self.__lg.debug('\t  - {} Selected categories: {}'.format(len(self.__selected_category_lst), self.__selected_category_lst))

        product_data_lst = self.__model.products_from_categories(self.__selected_category_lst)
        self.__update_view_product('product', product_data_lst)

    def __update_data_selected_product(self, selected_item, deselected_item):
        print(' >   Enter into __update_data_selected_product function')

        product_code = selected_item.indexes()[1].data(Qt.UserRole+1)

        print('selected product:', selected_item.indexes()[1].data(), product_code )

        product_data_dct = self.__model.products([product_code])
        
        category_lst = self.__model.category_data(product_data_dct[product_code]['categories_hierarchy'])

        altern_category_cbox = self.ui.altern_category_cbox

        altern_category_cbox.blockSignals(True)
        altern_category_cbox.clear()

        for category_dct in category_lst:

            # altern_category_cbox.insertItem(-1, category_data['name'], category_id)
            altern_category_cbox.addItem(category_dct['name'], category_dct['id'])

        cnt = altern_category_cbox.count()
        if cnt > 0:
            altern_category_cbox.setCurrentIndex(cnt-1)

        altern_category_cbox.blockSignals(False)

        self.__update_data_alternative_product(altern_category_cbox.currentIndex())


    def __update_data_alternative_product(self, category_index):

        print(' >   Enter into __update_data_alternative_product function')
        product_code = self.ui.product_view.selectionModel().selectedIndexes()[1].data(Qt.UserRole+1)
        
        category_id = self.ui.altern_category_cbox.itemData(category_index)
        # category_id = self.ui.altern_category_cbox.currentData()
        print('From category: {}; Compare alternative product with #{}'.format(category_id, product_code))
        

        product_data_lst = self.__model.alternative_products(product_code, category_id)
        self.__update_view_product('alternative', product_data_lst)

    def __add_product_2_favorite(self, is_checked=False):
        
        indexes = self.ui.product_view.selectionModel().selectedIndexes()
        
        self.__set_favorite(indexes, True)

    def __add_alternative_2_favorite(self, is_checked=False):

        indexes = self.ui.alternative_view.selectionModel().selectedIndexes()
        
        self.__set_favorite(indexes, True)

    def __remove_favorite(self, is_checked=False):

        indexes = self.ui.favorite_view.selectionModel().selectedIndexes()
        
        self.__set_favorite(indexes, False)

    def __set_favorite(self, indexes, is_added):

        if indexes:
            
            product_code = indexes[1].data(Qt.UserRole+1)
            print(" -  push_button select product #{}-{}".format(product_code, indexes[1].data()))

            self.__model.set_favorite(product_code, is_added)

            product_data_lst = self.__model.products_from_categories([], is_favorite=True)        
            self.__update_view_product('favorite', product_data_lst)

        else:
            print(" -  No selected product ")


if __name__ == "__main__":

    # add 'model' package
    sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'z_model'))
    from fact import ZFact as ZModel


    app = QApplication(sys.argv)


    model = ZModel()

    ui = ZOpynFacts_View(model)
    ui.show()

#    ui = QDialog()
#    f = Ui_Form()
#    f.setupUi(ui)
#    ui.show()

    sys.exit( app.exec_() )