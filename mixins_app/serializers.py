from .models import Teacher,Student,Atendence
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class Attendenceserializer(serializers.ModelSerializer):
    class Meta:
        model=Atendence
        fields='__all__'
