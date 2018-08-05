from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/usuario/login/')
def view_esqueceu_senha(request):
    return render(request, 'esqueceu_senha.html')
