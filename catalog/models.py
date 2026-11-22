from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)    #max len of category name is 100 chars

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)    #max len of tag name is 100 chars

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)    #max len of product name is 100 chars
    description = models.TextField()            #description of product
    price = models.DecimalField(max_digits=10, decimal_places=2)  #price

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  #category of product - there's alwasy only one category for a product
    tags = models.ManyToManyField(Tag, blank=True)    #tags for the product - a product can have many tags and a tag can be associated to many products

    def __str__(self):
        return self.name


