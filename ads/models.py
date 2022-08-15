from django.db import models


class Ad(models.Model):
    # STATUS = [
    #     ("draft", "черновик"),
    #     ("open", "открыто"),
    #     ("closed", "в архиве")
    # ]
    # slag = models.SlugField(max_length=50)
    # status = models.CharField(max_length=6, choices=STATUS, default="draft")

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=2000)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.DateField(auto_now_add=True)


class Category(models.Model):
    # slag = models.SlugField(max_length=50)

    name = models.CharField(max_length=100)
