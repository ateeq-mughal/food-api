# Generated by Django 3.2.7 on 2022-02-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0007_order_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(related_name='order', to='foodapi.OrderItem'),
        ),
    ]
