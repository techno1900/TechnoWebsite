from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog,name="blog"),
    path('artical/<str:pk>/',views.artical,name="artical"),
]