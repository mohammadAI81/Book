# Generated by Django 5.0 on 2024-02-08 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_author_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='books.author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_book', to='books.book'),
        ),
    ]