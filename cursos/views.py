from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Avaliation
from .serializers import CourseSerializer, AvaliationSerializer

class CourseAPIView(APIView):
    """
    API of Course
    """
    def get(self, request):
        print(dir(request))
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

class AvalaitionAPIView(APIView):
    """
    API of Avaliations
    """
    def get(self, request):
        avaliations = Avaliation.objects.all()
        serializer = AvaliationSerializer(avaliations, many=True)
        return Response(serializer.data)