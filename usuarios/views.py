from django.shortcuts import render


def view_login(request):
    return render(request, 'login.html')

def view_esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

def view_index(request):
    return render(request, 'index.html')

def view_cadastro_animal(request):
    return render(request, 'cadastro_de_animal.html')
