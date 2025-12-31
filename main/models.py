from django.db import models

class Item(models.Model):
    slug = models.SlugField('Unique URL identifier', unique=True)
    title = models.CharField('Product title', max_length=200)
    image = models.CharField('Product image URL', max_length=50)
    desc = models.TextField('Product description')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title