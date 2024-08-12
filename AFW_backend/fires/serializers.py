# fires/serializers.py

from rest_framework import serializers
from .models import WildfireReport

class FireReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WildfireReport
        fields = '__all__'