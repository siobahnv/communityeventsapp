# Generated by Django 2.2 on 2019-04-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190411_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='execution_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]