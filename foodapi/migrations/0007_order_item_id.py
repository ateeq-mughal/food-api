# Generated by Django 3.2.7 on 2022-02-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0006_rename_food_order_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item_id',
            field=models.TextField(null=True),
        ),
    ]
