from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    page_count = models.IntegerField()
    category = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return f"{self.name} by {self.author_name}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
