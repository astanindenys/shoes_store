# Generated by Django 5.0.1 on 2024-01-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_size_product_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['name']},
        ),
    ]
