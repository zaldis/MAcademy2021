# Generated by Django 3.2.8 on 2021-12-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_reader_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='book_photos'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveIntegerField(default=1600, verbose_name='publication year'),
        ),
    ]
