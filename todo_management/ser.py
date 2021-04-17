from rest_framework import serializers
from .models import Todo
# from accounts.ser import ShortUserSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task']

