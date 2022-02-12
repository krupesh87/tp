# Generated by Django 2.2.7 on 2021-09-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashokapp', '0005_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='Address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]