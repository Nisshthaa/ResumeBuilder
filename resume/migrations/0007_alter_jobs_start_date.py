# Generated by Django 4.2.13 on 2024-08-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_internship_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]