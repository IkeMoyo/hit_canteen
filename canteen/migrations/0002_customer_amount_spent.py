# Generated by Django 3.1.1 on 2022-05-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='amount_spent',
            field=models.FloatField(default=0.0),
        ),
    ]
