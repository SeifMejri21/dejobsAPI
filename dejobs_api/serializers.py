from rest_framework import serializers

from dejobs_api.models import Companies, Jobs


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('company_id', 'name', 'symbol', 'long_description', 'short_description',
                  'service_type', 'alchemy_page', 'careers_page', 'hr_provider', 'hr_page', 'hr_email','website', 'logo',
                  'twitter', 'tags', 'chains',)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('job_id', 'title', 'location', 'apply_url', 'company_name', 'company_symbol')
