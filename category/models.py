from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
