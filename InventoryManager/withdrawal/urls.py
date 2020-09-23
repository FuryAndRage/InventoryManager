from django.urls import path
from . import views


app_name = 'withdrawal'
urlpatterns = [
    path('', views.withdrawal_log, name = 'log')
]