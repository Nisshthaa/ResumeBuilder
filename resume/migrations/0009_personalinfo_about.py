# Generated by Django 4.2.13 on 2024-08-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_certification_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='about',
            field=models.TextField(default='Default about text'),
        ),
    ]
