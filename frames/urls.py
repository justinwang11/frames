from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^wireframe1/$', views.wireframe1, name='wireframe1'),
    url(r'^wireframe1_new/', views.wireframe1_new, name='wireframe1_new'),
    url(r'^wireframe2/$', views.wireframe2, name='wireframe2'),
    url(r'^wireframe2_new/', views.wireframe2_new, name='wireframe2_new'),
    url(r'^wireframe3/$', views.wireframe3, name='wireframe3'),
    url(r'^wireframe3_new/', views.wireframe3_new, name='wireframe3_new'),
    url(r'^wireframe4/$', views.wireframe4, name='wireframe4'),
    url(r'^wireframe4_new/', views.wireframe4_new, name='wireframe4_new'),
    url(r'^wireframe5/$', views.wireframe5, name='wireframe5'),
]
