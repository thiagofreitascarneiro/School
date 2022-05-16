from django.urls import path

from .views import CourseAPIView, AvalaitionAPIView

urlpatters = [
    path('course/', CourseAPIView.as_view(), name='courses'),
    path('avalition/', AvalaitionAPIView.as_view(), name='avaliations'),
]