# Generated by Django 4.2.7 on 2023-11-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
