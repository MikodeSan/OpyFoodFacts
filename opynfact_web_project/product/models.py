from django.db import models


class ZContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


class ZProduct(models.Model):
    reference = models.IntegerField('Code', null=True)
    brand = models.CharField('Marque', max_length=200)
    name = models.CharField(max_length=200)
    store = models.IntegerField(null=True)
    category_hierarchy = models.IntegerField(null=True)
    nutrition_grade = models.IntegerField(null=True)
    nova_group = models.IntegerField(null=True)
    url = models.URLField()
    picture = models.URLField()
    last_modified = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    isSearched = models.BooleanField(default=False)
    firstSearchDate = models.DateTimeField(auto_now_add=True)
    lastSearchDate = models.DateTimeField(auto_now_add=True)
    
    isfavorite = models.BooleanField(default=False)

    contact = models.ManyToManyField(ZContact, related_name='favorite', blank=True)
    alternative = models.ManyToManyField('self', related_name='product_b', blank=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return str(self.name)


class ZCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    product = models.ManyToManyField(ZProduct, related_name='category', blank=True)

    def __str__(self):
        return self.name


# class Booking(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     contacted = models.BooleanField(default=False)
#     album = models.OneToOneField(Album)
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)