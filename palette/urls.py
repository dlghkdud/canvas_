from django.urls import path

from . import views

app_name = 'palette'

urlpatterns = [
    path('', views.index, name='index'), 
    path('start/',views.start, name='start'),
    path('<int:drawing_id>/', views.detail, name='detail'),
    path('comment/create/<int:drawing_id>/', views.comment_create, name='comment_create'),
    path('drawing/create/', views.drawing_create, name='drawing_create'),
    path('drawing/modify/<int:drawing_id>/', views.drawing_modify, name='drawing_modify'),
    path('drawing/delete/<int:drawing_id>/', views.drawing_delete, name='drawing_delete'),
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('drawing/vote/<int:drawing_id>/', views.drawing_vote, name='drawing_vote'),
    path('drawing/<int:id>/download/', views.file_download, name='file_download'),
]