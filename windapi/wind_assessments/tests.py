"""
Tests for models.
"""
from django.test import TestCase
from wind_assessments.models import WindAssessment
from django.contrib.auth import get_user_model
from decimal import Decimal
# Create your tests here.


class WindAssessmentModelTests(TestCase):
    """Test Wind Assessment model."""

    def test_create_wind_assessment(self):
        """Test creating a wind assessment is successful."""
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        wind_assessment = WindAssessment.objects.create(
            user=user,
            location='Test Location',
            date='2024-09-15',
            wind_speed=Decimal('15.50'),
            wind_direction='NE',
            temperature=Decimal('22.5'),
            assessment_notes='Sample notes for the wind assessment.'
        )

        self.assertEqual(
            str(wind_assessment),
            f"Assess for {wind_assessment.location} on {wind_assessment.date}"
            )
