# Generated by Django 5.0.7 on 2024-07-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='warehouse',
            field=models.CharField(default='', max_length=200),
        ),
    ]
