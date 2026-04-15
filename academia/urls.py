from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('alunos/', views.alunos),
    path('editar-aluno/<int:id>/', views.editar_aluno),
    path('deletar-aluno/<int:id>/', views.deletar_aluno),

    path('exercicios/', views.exercicios),
    path('editar-exercicio/<int:id>/', views.editar_exercicio),
    path('deletar-exercicio/<int:id>/', views.deletar_exercicio),

    path('treinos/', views.treinos),
    path('deletar-treino/<int:id>/', views.deletar_treino),

    # API
    path('api/alunos/', views.api_alunos),
    path('api/exercicios/', views.api_exercicios),
    path('api/treinos/', views.api_treinos),
]