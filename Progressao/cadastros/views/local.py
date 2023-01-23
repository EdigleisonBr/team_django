from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Este decoretor obriga o usuário estar registrado para entrar em determinada função.

from ..models import Local, Jogo
from ..forms import LocalForm


# Listar
@login_required
def localListar(request):

    locais = Local.objects.all().order_by('id')
        
    # paginator = Paginator(tasks_list, 6) # (Lista das tarefas, nº de exibição por página).
    # page = request.GET.get('page') # Resgata o argumento page do Request.
    # tasks = paginator.get_page(page) # Exibe os elementos da página correta. 

    return render(request, 'cadastros/local/listar.html', {'locais': locais})


# Criar
@login_required
def localCriar(request):
    aba = 'Local'
    titulo = 'Cadastrar Local'
    if request.method == 'POST':
        form = LocalForm(request.POST)
        
        if form.is_valid():
            local = form.save(commit=False) # (commit=False) para o processo de salvamento para executar a linha de baixo.
            local.save()
            messages.success(request, 'Cadastro salvo com sucesso.')
            return redirect('/listar/locais/')
    else:
        form = LocalForm()
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Editar
@login_required
def localEditar(request, id):
    aba = 'Local'
    titulo = 'Cadastrar Local'
    local = get_object_or_404(Local, pk=id)
    form = LocalForm(instance=local)

    if (request.method == 'POST'):
        form = LocalForm(request.POST, instance=local)
        if(form.is_valid()):
            local.save()
            messages.info(request, 'Cadastro editado com sucesso.')
            return redirect('/listar/locais/')
        else:
            return render(request, 'cadastros/form.html', {'form': form, 'local': local})    
    else:
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Deletar
@login_required
def localDeletar(request, id):
    local = get_object_or_404(Local, pk=id)
    busca_local = Jogo.objects.filter(local=id)

    if busca_local:
        messages.warning(request, f'{local.nome} não pode ser deletado pois já está cadastrado em Jogos!')
    else:
        local.delete()
        messages.warning(request, 'Local deletado com sucesso.')
 
    return redirect('/listar/locais/')