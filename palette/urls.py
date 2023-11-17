from django.urls import path

from . import views

app_name = 'palette'

urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:drawing_id>/', views.detail, name='detail'),
    path('comment/create/<int:drawing_id>/', views.comment_create, name='comment_create'),
    path('drawing/create/', views.drawing_create, name='drawing_create'),
    path('drawing/modify/<int:drawing_id>/', views.drawing_modify, name='drawing_modify'),
]