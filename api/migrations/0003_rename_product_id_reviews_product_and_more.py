# Generated by Django 4.1.7 on 2023-03-13 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_reviews_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='user_id',
            new_name='user',
        ),
    ]
