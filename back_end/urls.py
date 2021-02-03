from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from project_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lists, name='HomePage'),
    path('predict/', views.predict, name='predict'),
    path('display/', views.display, name='display'),
]
