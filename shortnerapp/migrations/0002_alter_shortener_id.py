# Generated by Django 3.2.6 on 2021-09-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortnerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
