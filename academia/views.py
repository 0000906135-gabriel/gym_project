from django.shortcuts import render, redirect
from .models import Aluno, Exercicio, Treino


def alunos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')

        Aluno.objects.create(nome=nome, email=email, idade=idade)

    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})


def exercicios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        Exercicio.objects.create(nome=nome, descricao=descricao)

    exercicios = Exercicio.objects.all()
    return render(request, 'exercicios.html', {'exercicios': exercicios})


def treinos(request):
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        exercicio_id = request.POST.get('exercicio')
        series = request.POST.get('series')
        repeticoes = request.POST.get('repeticoes')

        Treino.objects.create(
            aluno_id=aluno_id,
            exercicio_id=exercicio_id,
            series=series,
            repeticoes=repeticoes
        )

    treinos = Treino.objects.all()
    alunos = Aluno.objects.all()
    exercicios = Exercicio.objects.all()

    return render(request, 'treinos.html', {
        'treinos': treinos,
        'alunos': alunos,
        'exercicios': exercicios
    })