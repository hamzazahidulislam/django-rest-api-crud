from rest_framework import serializers
from .models import Task,My

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class Myserilizer(serializers.ModelSerializer):
    model = My
    fields = '__all__'