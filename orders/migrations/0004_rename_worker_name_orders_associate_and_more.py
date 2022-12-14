# Generated by Django 4.1.1 on 2022-10-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orders_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='worker_name',
            new_name='associate',
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('tak', 'TAK'), ('nie', 'NIE')], default='nie', max_length=3),
        ),
    ]
