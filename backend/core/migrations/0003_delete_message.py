# Generated by Django 4.2.2 on 2023-07-12 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_order_created_at_order_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
