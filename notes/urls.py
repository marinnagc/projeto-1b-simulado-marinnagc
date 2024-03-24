from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("editar/<int:id>", views.editar, name='editar'),
    path("delete/<int:id>", views.delete, name="delete"),
    path('tags/', views.lista_tags, name='lista_tags'),
    path('links/<int:id>/', views.links, name='links'),
    path('facts/', views.facts, name='facts'),
    path("curtir/<int:id>", views.curtir, name="curtir"),
]