from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('alunos/', views.alunos),
    path('editar-aluno/<int:id>/', views.editar_aluno),
    path('deletar-aluno/<int:id>/', views.deletar_aluno),

    path('exercicios/', views.exercicios),
    path('treinos/', views.treinos),
]