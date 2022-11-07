

from django.contrib import admin
from django.urls import path
from researches import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list, name='list' ),
    path('add/', views.add, name='create'),
]
