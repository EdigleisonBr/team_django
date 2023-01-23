from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Este decoretor obriga o usuário estar registrado para entrar em determinada função.

from ..models import Atleta, Gol
from ..forms import AtletaForm


# Listar
@login_required
def atletaListar(request):

    atletas = Atleta.objects.all().order_by('nome')

    # paginator = Paginator(tasks_list, 6) # (Lista das tarefas, nº de exibição por página).
    # page = request.GET.get('page') # Resgata o argumento page do Request.
    # tasks = paginator.get_page(page) # Exibe os elementos da página correta. 

    return render(request, 'cadastros/atleta/listar.html', {'atletas': atletas})


# Criar
@login_required
def atletaCriar(request):
    aba = 'Atleta'
    titulo = 'Cadastrar Atleta'
    if request.method == 'POST':
        form = AtletaForm(request.POST)
        
        if form.is_valid():
            atleta = form.save(commit=False) # (commit=False) para o processo de salvamento para executar a linha de baixo.
            atleta.save()
            messages.success(request, 'Cadastro salvo com sucesso.')
            return redirect('/listar/atletas/')
    else:
        form = AtletaForm()
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Editar
@login_required
def atletaEditar(request, id):
    aba = 'Atleta'
    titulo = 'Cadastrar Atleta'
    atleta = get_object_or_404(Atleta, pk=id)
    form = AtletaForm(instance=atleta)
    
    if (request.method == 'POST'):
        form = AtletaForm(request.POST, instance=atleta)
        if(form.is_valid()):
            atleta.save()
            messages.info(request, 'Cadastro editado com sucesso.')
            return redirect('/listar/atletas/')
        else:
            return render(request, 'cadastros/form.html', {'form': form, 'atleta': atleta})    
    else:
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Deletar
@login_required
def atletaDeletar(request, id):
    atleta = get_object_or_404(Atleta, pk=id)
    busca_atleta = Gol.objects.filter(atleta=id)
        
    if busca_atleta:
        messages.warning(request, f'Atleta {atleta.nome} não pode ser deletado pois já possui gols cadastrados!')
    else:
        atleta.delete()
        messages.success(request, 'Atleta removido com sucesso.')

    return redirect('/listar/atletas/')