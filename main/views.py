from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def cadastro_funcionario(request):
    return render(request, 'cadastro_funcionario.html')


def cadastro_assistido(request):
    return render(request, 'cadastro_assistido.html')


def template_base(request):
    return render(request, 'template_base.html')


def agendamento(request):
    return render(request, 'agendamento.html')