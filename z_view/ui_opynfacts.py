# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z_view\form.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.select_all_btn = QtWidgets.QPushButton(self.groupBox_8)
        self.select_all_btn.setObjectName("select_all_btn")
        self.horizontalLayout_5.addWidget(self.select_all_btn)
        self.verticalLayout_2.addWidget(self.groupBox_8)
        self.category_view = QtWidgets.QTreeView(self.groupBox_6)
        self.category_view.setObjectName("category_view")
        self.verticalLayout_2.addWidget(self.category_view)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.product_view = QtWidgets.QTreeView(self.groupBox_7)
        self.product_view.setObjectName("product_view")
        self.verticalLayout_3.addWidget(self.product_view)
        self.horizontalLayout_2.addWidget(self.groupBox_7)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.alternative_view = QtWidgets.QListView(self.groupBox_4)
        self.alternative_view.setObjectName("alternative_view")
        self.horizontalLayout_3.addWidget(self.alternative_view)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.favorite_view = QtWidgets.QListView(self.groupBox_5)
        self.favorite_view.setObjectName("favorite_view")
        self.horizontalLayout_4.addWidget(self.favorite_view)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_10)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox_10)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.groupBox_10)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_10)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.verticalLayout_4.addWidget(self.groupBox_10)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_4.addWidget(self.groupBox_11)
        self.horizontalLayout_4.addWidget(self.groupBox_9)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 4, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.altern_category_cbox = QtWidgets.QComboBox(self.groupBox_2)
        self.altern_category_cbox.setObjectName("altern_category_cbox")
        self.gridLayout.addWidget(self.altern_category_cbox, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_3.setTitle(_translate("Form", "Selection"))
        self.groupBox_6.setTitle(_translate("Form", "Category"))
        self.select_all_btn.setText(_translate("Form", "Select All"))
        self.groupBox_7.setTitle(_translate("Form", "Product"))
        self.groupBox_4.setTitle(_translate("Form", "Alternative"))
        self.groupBox_5.setTitle(_translate("Form", "Favorite"))
        self.groupBox_9.setTitle(_translate("Form", "GroupBox"))
        self.groupBox_10.setTitle(_translate("Form", "GroupBox"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.groupBox_11.setTitle(_translate("Form", "GroupBox"))
        self.groupBox_2.setTitle(_translate("Form", "Criteria"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "Update db"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "Alternative category"))


