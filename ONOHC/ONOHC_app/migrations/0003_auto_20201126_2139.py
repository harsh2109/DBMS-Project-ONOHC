# Generated by Django 3.1.2 on 2020-11-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ONOHC_app', '0002_auto_20201126_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='Zip',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
