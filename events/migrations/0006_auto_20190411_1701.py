# Generated by Django 2.2 on 2019-04-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190411_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='execution_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='followup_w_nominee',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='sponsored',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='event_rating',
            field=models.CharField(choices=[('MS', 'Must sponsor'), ('GS', "It'd be great to support"), ('OC', 'Only if we can'), ('JB', 'Just be aware this one is coming up')], default='JB', max_length=2),
        ),
    ]
