from rest_framework import viewsets
from .models import FireReport, TwitterReport
from .serializers import FireReportSerializer, TwitterReportSerializer

class FireReportViewSet(viewsets.ModelViewSet):
    queryset = FireReport.objects.all()
    serializer_class = FireReportSerializer

class TwitterReportViewSet(viewsets.ModelViewSet):
    queryset = TwitterReport.objects.all()
    serializer_class = TwitterReportSerializer