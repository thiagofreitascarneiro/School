from django.urls import path
from django.conf.urls import url


from .views import CourseAPIView, AvalaitionAPIView

urlpatterns = [
    path('cursos/', CourseAPIView.as_view(), name='cursos'),
    path('avalicoes/', AvalaitionAPIView.as_view(), name='avaliacoes'),
]