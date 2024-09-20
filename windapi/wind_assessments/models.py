"""
Database models for Wind Assessments.
"""
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Turbine(models.Model):
    """Model to represent a Turbine."""
    name = models.CharField(max_length=255)
    capacity = models.DecimalField(
        max_digits=6,
        decimal_places=2)  # Capacity in MW (e.g., 3.5 MW)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.capacity} MW)"


class WindAssessment(models.Model):
    REPORT_TYPE_CHOICES = [
        ('feasibility', 'Feasibility Assessment'),
        ('wind_resource', 'Wind Resource Assessment'),
        ('site_suitability', 'Site Suitability Assessment'),
    ]

    TURBINE_CHOICES = [
        ('turbine_model_a', 'Turbine Model A'),
        ('turbine_model_b', 'Turbine Model B'),
    ]

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    lat = models.DecimalField(max_digits=8, decimal_places=5, default=0.0)
    lon = models.DecimalField(
        max_digits=8,
        decimal_places=5,
        default=0.0)
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    turbine_type = models.CharField(
        max_length=20,
        choices=TURBINE_CHOICES)  # This is correct
    date = models.DateField()
    assessment_notes = models.TextField(null=True, blank=True)
    report_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Wind Assessment for {self.customer_name}"
