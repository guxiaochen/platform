from django.urls import path
from project_app import views

"""项目管理"""
urlpatterns = [

    path('', views.project),
    path('add_project/', views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),
    path('del_project/<int:pid>/', views.del_project),
]