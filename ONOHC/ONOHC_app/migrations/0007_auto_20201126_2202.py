# Generated by Django 3.1.2 on 2020-11-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ONOHC_app', '0006_auto_20201126_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='Zip',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
