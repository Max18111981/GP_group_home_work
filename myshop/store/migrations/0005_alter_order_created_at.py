# Generated by Django 5.1.4 on 2024-12-10 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cartitem_order_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 12, 10, 13, 45, 32, 315372, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
