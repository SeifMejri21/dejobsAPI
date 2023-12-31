from django.db import models


class Companies(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    symbol = models.CharField(max_length=255, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    service_type = models.CharField(max_length=255, null=True, blank=True)
    alchemy_page = models.URLField(null=True, blank=True)
    careers_page = models.URLField(null=True, blank=True)
    hr_provider = models.CharField(max_length=255, null=True, blank=True)
    hr_page = models.CharField(max_length=255, null=True, blank=True)
    hr_email = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    chains = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'companies'


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True, unique=True)
    job_code = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(max_length=255, null=True, blank=True)
    apply_url = models.URLField(null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_symbol = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    salary_range = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'jobs'
