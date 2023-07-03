from django.urls import path
from . import views

urlpatterns = [
   path('Check/<int:object_id>', views.Check, name='Check'),
]