from rest_framework import generics 
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets

from .models import Course, Avaliation
from .serializers import CourseSerializer, AvaliationSerializer

"""
API V1
"""


class CourseAllAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvaliationAllAPIView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
           return self.queryset.filter(id=self.kwargs.get('curso_pk')) 
        return self.queryset.all()


class AvaliationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), 
                                            id=self.kwargs.get('curso_pk'),
                                            pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
        

"""
API V2
"""

class CourceViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer