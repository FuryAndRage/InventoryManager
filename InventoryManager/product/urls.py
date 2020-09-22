from django.urls import path
from . import views
from InventoryManager.withdrawal import views as wdviews

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name = 'list'),
    path('search/', views.product_search, name='search'),
    path('add/', views.product_add, name = 'add'),
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('delete/<int:pk>/', views.product_delete, name = 'delete'),



    path('<int:pk>/withdrawal/', wdviews.withdrawal_product, name = 'withdrawal')
    
]