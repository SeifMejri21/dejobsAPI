# Generated by Django 3.2.21 on 2023-09-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dejobs_api', '0005_rename_company_type_companies_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='hr_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]