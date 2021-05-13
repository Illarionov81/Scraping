from rest_framework import serializers
from webapp.models import Data, Company


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        # exclude = ['id', 'company']


class CompanySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name='api_v1:company-detail')
    data_display = DataSerializer(many=True, read_only=True, source='data')

    class Meta:
        model = Company
        fields = ['name', 'url', 'data_display']
