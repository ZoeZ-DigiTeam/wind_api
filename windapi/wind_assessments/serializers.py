"""
Serializers for the Wind Assessment API view.
"""
# from django.utils.translation import gettext as _

from rest_framework import serializers
from wind_assessments.models import WindAssessment


class WindAssessmentSerializer(serializers.ModelSerializer):
    """Serializer for wind assessment objects."""

    class Meta:
        model = WindAssessment
        fields = [
            'id',
            'location',
            'date',
            'wind_speed',
            'wind_direction',
            'temperature',
            'assessment_notes']
        read_only_fields = ['id']
