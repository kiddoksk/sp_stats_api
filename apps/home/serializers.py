"""
Home App Serializers
"""
from rest_framework import serializers

from .models import UserDetails, StudentDetails


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User Detail serializer
    """

    class Meta:
        model = UserDetails
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    """
    Student Detail serializer
    """

    class Meta:
        model = StudentDetails
        fields = '__all__'
