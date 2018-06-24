from django.shortcuts import render


def view_esqueceu_senha(request):
    return render(request, 'esqueceu_senha.html')
