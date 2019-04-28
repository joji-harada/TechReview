from django.urls import path
from . import views

#takes proj urls include and transfers it to the views render request
urlpatterns=[
    path('', views.index, name='index'),
    path('getTypes/', views.getTypes, name='types')
]

