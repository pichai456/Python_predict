from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from project_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='HomePage'),
    path('predicts/', views.predicts, name='predicts'),
    # path('display/', views.display, name='display'),
]
