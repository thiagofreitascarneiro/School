from django.urls import path
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from .views import (
CourseAPIView, 
CourseAllAPIView, 
AvaliationAllAPIView, 
AvaliationAPIView,
CourceViewSet,
AvaliationViewSet
)

router = SimpleRouter()
router.register('cursos', CourceViewSet)
router.register('avaliacoes', AvaliationViewSet)


urlpatterns = [
    path('cursos/', CourseAllAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CourseAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliationAllAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliationAPIView.as_view(), name='curso_avaliacao'),
    
    path('avaliacoes/', AvaliationAllAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliationAPIView.as_view(), name='avaliacao'),
]