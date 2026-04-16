from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Aluno, Exercicio, Treino
import json


# 🏠 HOME
def home(request):
    return render(request, 'home.html')


# 👤 ALUNOS
def alunos(request):
    mensagem = None

    if request.method == 'POST':
        Aluno.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            idade=request.POST.get('idade')
        )
        mensagem = "Aluno criado com sucesso!"

    return render(request, 'alunos.html', {
        'alunos': Aluno.objects.all(),
        'mensagem': mensagem
    })


def editar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.email = request.POST.get('email')
        aluno.idade = request.POST.get('idade')
        aluno.save()
        return redirect('/alunos/')

    return render(request, 'editar_aluno.html', {'aluno': aluno})


def deletar_aluno(request, id):
    Aluno.objects.get(id=id).delete()
    return redirect('/alunos/')


# 🏋️ EXERCÍCIOS
def exercicios(request):
    mensagem = None

    if request.method == 'POST':
        Exercicio.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao')
        )
        mensagem = "Exercício criado com sucesso!"

    return render(request, 'exercicios.html', {
        'exercicios': Exercicio.objects.all(),
        'mensagem': mensagem
    })


def editar_exercicio(request, id):
    exercicio = Exercicio.objects.get(id=id)

    if request.method == 'POST':
        exercicio.nome = request.POST.get('nome')
        exercicio.descricao = request.POST.get('descricao')
        exercicio.save()
        return redirect('/exercicios/')

    return render(request, 'editar_exercicio.html', {'exercicio': exercicio})

def deletar_exercicio(request, id):
    Exercicio.objects.get(id=id).delete()
    return redirect('/exercicios/')


# 📋 TREINOS
def treinos(request):
    mensagem = None

    if request.method == 'POST':
        Treino.objects.create(
            aluno_id=request.POST.get('aluno'),
            exercicio_id=request.POST.get('exercicio'),
            series=request.POST.get('series'),
            repeticoes=request.POST.get('repeticoes')
        )
        mensagem = "Treino criado com sucesso!"

    return render(request, 'treinos.html', {
        'treinos': Treino.objects.all(),
        'alunos': Aluno.objects.all(),
        'exercicios': Exercicio.objects.all(),
        'mensagem': mensagem
    })


def deletar_treino(request, id):
    Treino.objects.get(id=id).delete()
    return redirect('/treinos/')


# 🌐 API ALUNOS
@csrf_exempt
def api_alunos(request):
    if request.method == "GET":
        data = list(Aluno.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        dados = json.loads(request.body)
        aluno = Aluno.objects.create(**dados)
        return JsonResponse({"id": aluno.id})


# 🌐 API EXERCÍCIOS
@csrf_exempt
def api_exercicios(request):
    if request.method == "GET":
        data = list(Exercicio.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        dados = json.loads(request.body)
        exercicio = Exercicio.objects.create(**dados)
        return JsonResponse({"id": exercicio.id})


# 🌐 API TREINOS
@csrf_exempt
def api_treinos(request):
    if request.method == "GET":
        data = list(Treino.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        dados = json.loads(request.body)
        treino = Treino.objects.create(**dados)
        return JsonResponse({"id": treino.id})