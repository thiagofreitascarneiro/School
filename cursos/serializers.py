from rest_framework import serializers

from .models import Course, Avaliation



class AvaliationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliation
        fields = (
            'id',
            'cource',
            'name',
            'email',
            'comment',
            'avaliation',
            'create',
            'active'
        )
    
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'create',
            'active'
        )