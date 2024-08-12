from rest_framework import viewsets
from .models import WildfireReport
from .serializers import FireReportSerializer

class WildfireViewSet(viewsets.ModelViewSet):
    queryset = WildfireReport.objects.all()
    serializer_class = FireReportSerializer

# class WildfireDetailViewSet(viewsets.ModelViewSet):
#     queryset = WildfireDetail.objects.all()
#     serializer_class = TwitterReportSerializer