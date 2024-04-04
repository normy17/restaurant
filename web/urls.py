from django.urls import path

from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('specializations/', specialization_add, name='specializations'),
    path('rest_add/', rest_add, name='rest_add'),
    path('<int:id>/edit/', rest_edit, name='rest_edit'),
    path('<int:id>/delete/', rest_delete, name='rest_delete'),
]