from rest_framework import serializers
from django.db.models import Avg

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
    
    def validate_avaliation(self, value):
        if value in range(1, 6):
            return value 
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 a 5.')
    
class CourseSerializer(serializers.ModelSerializer):
    ## Nested Relationship
    # avaliations = AvaliationSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliations = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='avaliation-detail'
    )

    media_avaliation = serializers.SerializerMethodField()

    # Primary Key Related Field
    # avaliations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'create',
            'active',
            'avaliations',
            'media_avaliation'
        )
    
    def get_media_avaliation(self, obj):
        media = obj.avaliations.aggregate(Avg('avaliation')).get('avaliation__avg')

        if media is None:
            return 0
        return round(media * 2) / 2