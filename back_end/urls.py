from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from project_App import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.index, name='HomePage'),
    url(r'predicts/', views.predicts, name='predicts'),
    
]
