# Generated by Django 5.0.2 on 2024-05-23 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_alter_size_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['created_at']},
        ),
    ]