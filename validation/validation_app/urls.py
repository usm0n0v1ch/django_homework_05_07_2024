from django.urls import path

from validation_app import views

urlpatterns=[
    path('',views.index,name='index')
]