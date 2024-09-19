# Generated by Django 3.2.25 on 2024-09-17 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WindAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_direction', models.CharField(max_length=255)),
                ('temperature', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('assessment_notes', models.TextField(blank=True, null=True)),
                ('report_url', models.URLField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
