from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonTimeLogsUin(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['uin']


# class PersonTimeLogsEmail(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['primary_email']
