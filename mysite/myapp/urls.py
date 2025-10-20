from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('abdullah/', views.abdullah, name='abdullah'),
    path('mohammed/', views.mohammed, name='mohammed'),
    path('<str:name>/', views.greet, name="greet"),
]
