from django import forms
from .models import WindAssessment

class WindAssessmentForm(forms.ModelForm):
    """Form for creating a new wind assessment."""

    class Meta:
        model = WindAssessment
        fields = ['location', 'date', 'wind_speed', 'wind_direction', 'temperature', 'assessment_notes']
