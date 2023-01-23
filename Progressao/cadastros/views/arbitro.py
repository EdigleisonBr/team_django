from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Este decoretor obriga o usuário estar registrado para entrar em determinada função.
import datetime

from ..models import Arbitro, Jogo
from ..forms import ArbitroForm


# Listar
@login_required
def arbitroListar(request):

    arbitros = Arbitro.objects.all().order_by('id')
        
    # paginator = Paginator(tasks_list, 6) # (Lista das tarefas, nº de exibição por página).
    # page = request.GET.get('page') # Resgata o argumento page do Request.
    # tasks = paginator.get_page(page) # Exibe os elementos da página correta. 

    return render(request, 'cadastros/arbitro/listar.html', {'arbitros': arbitros})


# Criar
@login_required
def arbitroCriar(request):
    aba = 'Arbitro'
    titulo = 'Cadastrar Arbitro'
    if request.method == 'POST':
        form = ArbitroForm(request.POST)
        
        if form.is_valid():
            arbitro = form.save(commit=False) # (commit=False) para o processo de salvamento para executar a linha de baixo.
            arbitro.save()
            messages.success(request, 'Cadastro salvo com sucesso.')
            return redirect('/listar/arbitros/')
    else:
        form = ArbitroForm()
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Editar
@login_required
def arbitroEditar(request, id):
    aba = 'Arbitro'
    titulo = 'Editar Árbitro'
    arbitro = get_object_or_404(Arbitro, pk=id)
    form = ArbitroForm(instance=arbitro)

    if (request.method == 'POST'):
        form = ArbitroForm(request.POST, instance=arbitro)
        if(form.is_valid()):
            arbitro.save()
            messages.info(request, 'Cadastro editado com sucesso.')
            return redirect('/listar/arbitros/')
        else:
            return render(request, 'cadastros/form.html', {'form': form, 'arbitro': arbitro})    
    else:
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Deletar
@login_required
def arbitroDeletar(request, id):
    arbitro = get_object_or_404(Arbitro, pk=id)
    busca_arbitro = Jogo.objects.filter(arbitro=id)

    if busca_arbitro:
        messages.warning(request, f'Árbitro {arbitro.nome} não pode ser deletado pois já está cadastrado em Jogos!')
    else:
        arbitro.delete()
        messages.warning(request, 'Árbitro deletado com sucesso.')
 
    return redirect('/listar/arbitros/')