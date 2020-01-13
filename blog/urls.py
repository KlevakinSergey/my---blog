from django.urls import  path
from . import views
from django.conf.urls import url











urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^add_simple_photo/$', views.add_simple_photo, name='add_simple_photo'),
    

   
    

]