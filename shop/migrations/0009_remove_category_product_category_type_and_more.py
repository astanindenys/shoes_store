# Generated by Django 5.0.1 on 2024-01-07 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_type_shop_type_name_6853a0_idx_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='shop.type'),
        ),
    ]
