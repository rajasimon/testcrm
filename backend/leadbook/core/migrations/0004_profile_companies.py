# Generated by Django 2.1.5 on 2019-01-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190117_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='companies',
            field=models.ManyToManyField(to='core.Company'),
        ),
    ]