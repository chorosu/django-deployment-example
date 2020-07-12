from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index2',views.index2,name='index2'),
    path('form_page',views.form_page,name='form_page')
]