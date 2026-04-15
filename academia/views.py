from django.shortcuts import render, redirect
from .models import Aluno, Exercicio, Treino


# 🏠 HOME
def home(request):
    return render(request, 'home.html')


# 👤 ALUNOS
def alunos(request):
    if request.method == 'POST':
        Aluno.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            idade=request.POST.get('idade')
        )

    return render(request, 'alunos.html', {
        'alunos': Aluno.objects.all()
    })


def deletar_aluno(request, id):
    Aluno.objects.get(id=id).delete()
    return redirect('/alunos/')


def editar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.email = request.POST.get('email')
        aluno.idade = request.POST.get('idade')
        aluno.save()
        return redirect('/alunos/')

    return render(request, 'editar_aluno.html', {'aluno': aluno})


# 🏋️ EXERCÍCIOS
def exercicios(request):
    if request.method == 'POST':
        Exercicio.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao')
        )

    return render(request, 'exercicios.html', {
        'exercicios': Exercicio.objects.all()
    })


# 📋 TREINOS
def treinos(request):
    if request.method == 'POST':
        Treino.objects.create(
            aluno_id=request.POST.get('aluno'),
            exercicio_id=request.POST.get('exercicio'),
            series=request.POST.get('series'),
            repeticoes=request.POST.get('repeticoes')
        )

    return render(request, 'treinos.html', {
        'treinos': Treino.objects.all(),
        'alunos': Aluno.objects.all(),
        'exercicios': Exercicio.objects.all()
    })