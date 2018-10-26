from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('form/', views.form_new, name="form_new"),
    path('form_detail/<int:pk>/', views.Details.as_view(), name='form_detail'),
    path('form/<int:pk>/edit/', views.form_edit, name='form_edit'),
    path('customer_list/', views.Customers_list.as_view(), name='customer_list'),
    path('room_detail/<int:number>/', views.Room_details.as_view(), name='room_detail'),
    path('room_list/', views.Room_list.as_view(), name='room_list'),
]