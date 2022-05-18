from rest_framework import generics 

from .models import Course, Avaliation
from .serializers import CourseSerializer, AvaliationSerializer


class CourseAllAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvaliationAllAPIView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

class AvaliationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer