"""
Views for the Wind Assessment API endpoint.
"""

from rest_framework import generics, authentication, permissions
from wind_assessments.models import WindAssessment
from wind_assessments.serializers import WindAssessmentSerializer
from rest_framework.permissions import IsAuthenticated


class CreateWindAssessmentView(generics.CreateAPIView):
    queryset = WindAssessment.objects.all()
    serializer_class = WindAssessmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListWindAssessmentView(generics.ListAPIView):
    """List all wind assessments for the authenticated user."""
    serializer_class = WindAssessmentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return wind assessments for the authenticated user."""
        return WindAssessment.objects.filter(user=self.request.user)


class RetrieveUpdateWindAssessmentView(generics.RetrieveUpdateAPIView):
    """Retrieve or update a specific wind assessment."""
    serializer_class = WindAssessmentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = WindAssessment.objects.all()

    def get_queryset(self):
        """Return wind assessments for the authenticated user."""
        return WindAssessment.objects.filter(user=self.request.user)
