# Generated by Django 5.0.4 on 2024-04-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_book_author_name_alter_book_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(help_text='Enter the name of the author', max_length=255, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(help_text='Enter the category of the book', max_length=255, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='', help_text='Enter a description of the book', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload an image of the book cover', null=True, upload_to='books/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(help_text='Enter the name of the book', max_length=255, verbose_name='Book Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(blank=True, help_text='Enter the number of pages in the book', null=True, verbose_name='Page Count'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Enter the price of the book', max_digits=6, verbose_name='Price'),
        ),
    ]
