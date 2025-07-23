from rest_framework import serializers
from .models import ApiTarget

class ApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTarget
        fields = ['interval_minutes', 'api', 'start_test', 'finish_test']

