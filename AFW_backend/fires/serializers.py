# fires/serializers.py

from rest_framework import serializers
from .models import FireReport, TwitterReport

class FireReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireReport
        fields = '__all__'

class TwitterReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterReport
        fields = '__all__'

# fires/views.py

from rest_framework import viewsets
from .models import FireReport, TwitterReport
from .serializers import FireReportSerializer, TwitterReportSerializer

class FireReportViewSet(viewsets.ModelViewSet):
    queryset = FireReport.objects.all()
    serializer_class = FireReportSerializer

class TwitterReportViewSet(viewsets.ModelViewSet):
    queryset = TwitterReport.objects.all()
    serializer_class = TwitterReportSerializer
