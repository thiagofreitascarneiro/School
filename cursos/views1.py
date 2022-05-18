from logging import raiseExceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Avaliation
from .serializers import CourseSerializer, AvaliationSerializer

class CourseAPIView(APIView):
    """
    API of Course
    """
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AvalaitionAPIView(APIView):
    """
    API of Avaliations
    """
    def get(self, request):
        avaliations = Avaliation.objects.all()
        serializer = AvaliationSerializer(avaliations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)