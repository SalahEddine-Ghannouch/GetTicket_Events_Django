from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Cart', views.UserCart, name='Cart'),
    path('CartCheckout', views.CartCheckout, name='CartCheckout'),
    path('search/', views.searchEvents, name='searchEvents'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('checkAll/', views.checkAll, name='checkAll'),
    path('rmoveitem/', views.rmoveitem, name='rmoveitem'),
    path('feedback/', views.feedback, name='feedback'),

]
