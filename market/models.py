from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Book Name'), help_text=_('Enter the name of the book'))
    page_count = models.IntegerField(null=True, blank=True, verbose_name=_('Page Count'), help_text=_('Enter the number of pages in the book'))
    category = models.CharField(max_length=255, verbose_name=_('Category'), help_text=_('Enter the category of the book'))
    author_name = models.CharField(max_length=255, verbose_name=_('Author'), help_text=_('Enter the name of the author'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Price'), help_text=_('Enter the price of the book'))
    image = models.ImageField(upload_to='books/', null=True, blank=True, verbose_name=_('Image'), help_text=_('Upload an image of the book cover'))
    description = models.TextField(default='', verbose_name=_('Description'), help_text=_('Enter a description of the book'))

    def __str__(self):
        return f"{self.name} by {self.author_name}"

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
