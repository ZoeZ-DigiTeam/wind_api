"""
Tests for models.
"""
from django.test import TestCase
from wind_assessments.models import WindAssessment, Turbine
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

        # Creating a wind assessment with the turbine type
        wind_assessment = WindAssessment.objects.create(
            user=user,
            customer_name='Test Customer',
            site_name='Test Site',
            report_type='feasibility',  # Based on your choices
            lat=Decimal('35.12345'),
            lon=Decimal('-120.12345'),
            location='Test Location',
            turbine_type='turbine_model_a',  # Use turbine_type instead of turbine instance
            date='2024-09-15',
            assessment_notes='Sample notes for the wind assessment.'
        )

        self.assertEqual(
            str(wind_assessment),
            f"Wind Assessment for {wind_assessment.customer_name} at {wind_assessment.site_name} on {wind_assessment.date}"
        )
