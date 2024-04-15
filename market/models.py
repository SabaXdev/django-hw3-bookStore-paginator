from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Book Name')
    page_count = models.IntegerField(null=True, blank=True, verbose_name='Page Count')
    category = models.CharField(max_length=255, verbose_name='Category')
    author_name = models.CharField(max_length=255, verbose_name='Author')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='books/', null=True, blank=True, verbose_name='Image')
    description = models.TextField(default='', verbose_name='Description')

    def __str__(self):
        return f"{self.name} by {self.author_name}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
