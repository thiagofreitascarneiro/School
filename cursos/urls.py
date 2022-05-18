from django.urls import path
from django.conf.urls import url


from .views import CourseAPIView, CourseAllAPIView, AvaliationAllAPIView, AvaliationAPIView

urlpatterns = [
    path('cursos/', CourseAllAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliationAllAPIView.as_view(), name='avaliacoes'),
    path('cursos/<int:pk>/', CourseAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>/', AvaliationAPIView.as_view(), name='avaliacao'),
]