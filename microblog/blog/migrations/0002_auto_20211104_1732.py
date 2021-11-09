# Generated by Django 3.2.8 on 2021-11-04 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveIntegerField(verbose_name='publication year'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(primary_key=True, serialize=False, verbose_name='title'),
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.ForeignKey(db_column='book_title', on_delete=django.db.models.deletion.CASCADE, to='blog.book', verbose_name='link to book')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='link to user')),
            ],
            options={
                'verbose_name': 'reader',
                'verbose_name_plural': 'readers',
            },
        ),
    ]