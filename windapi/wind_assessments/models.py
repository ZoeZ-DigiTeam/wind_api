"""
Database models for Wind Assessments.
"""
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class WindAssessment(models.Model):
    """Model for wind assessments."""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    location = models.CharField(max_length=255)
    date = models.DateField()
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_direction = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    assessment_notes = models.TextField(null=True, blank=True)
    report_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Wind Assessment for {self.location} on {self.date}"
