from rest_framework import generics 
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

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

    """
        detail : True to create router cource avalaiacoes
        methods: mermission methods accept
    """

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliation.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
          serializer = AvaliationSerializer(page, many=True)  
          return self.get_paginated_response(serializer.data)

        serializer = AvaliationSerializer(avaliacoes, many=True)
        return Response(serializer.data)

# class AvaliationViewSet(viewsets.ModelViewSet):
#     queryset = Avaliation.objects.all()
#     serializer_class = AvaliationSerializer

class AvaliationViewSet(
    # mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
