# Generated by Django 4.2.13 on 2024-08-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_personalinfo_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='about',
            field=models.TextField(default='tell about yourself'),
        ),
    ]
