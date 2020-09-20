from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name = 'list'),
    path('add/', views.product_add, name = 'add'),
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('search/', views.product_search, name='search')
]