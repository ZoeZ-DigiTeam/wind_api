"""
Serializers for the Wind Assessment API view.
"""
# from django.utils.translation import gettext as _

from rest_framework import serializers
from wind_assessments.models import WindAssessment, Turbine


class TurbineSerializer(serializers.ModelSerializer):
    """Serializer for turbine objects."""

    class Meta:
        model = Turbine
        fields = ['id', 'name', 'capacity']


class WindAssessmentSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = WindAssessment
        fields = [
            'user',
            'customer_name',
            'site_name',
            'report_type',
            'lat',
            'lon',
            'location',
            'turbine_type',
            'assessment_notes',
            'report_url',
            'date'
        ]
