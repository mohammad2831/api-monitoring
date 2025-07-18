from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.ApiView.as_view(), name='api'),
    #path('register/', views.register_user, name='register_user'),
]