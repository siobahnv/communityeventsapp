# Generated by Django 2.2 on 2019-04-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20190412_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='primary_goals',
            field=models.TextField(blank=True, null=True),
        ),
    ]