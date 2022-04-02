from rest_framework import serializers
from .models import StudentPlacements


class StudentPlacementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPlacements
        fields = '__all__'
