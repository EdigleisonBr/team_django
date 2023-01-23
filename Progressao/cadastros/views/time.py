from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Este decoretor obriga o usuário estar registrado para entrar em determinada função.

from ..models import Time, Jogo
from ..forms import TimeForm


# Listar
@login_required
def timeListar(request):

    times = Time.objects.all().order_by('nome')
        
    # paginator = Paginator(tasks_list, 6) # (Lista das tarefas, nº de exibição por página).
    # page = request.GET.get('page') # Resgata o argumento page do Request.
    # tasks = paginator.get_page(page) # Exibe os elementos da página correta. 

    return render(request, 'cadastros/time/listar.html', {'times': times})


# Criar
@login_required
def timeCriar(request):
    aba = 'Time'
    titulo = 'Cadastrar Time'
    if request.method == 'POST':
        form = TimeForm(request.POST)
        
        if form.is_valid():
            time = form.save(commit=False) # (commit=False) para o processo de salvamento para executar a linha de baixo.
            time.save()
            messages.success(request, 'Cadastro salvo com sucesso.')
            return redirect('/listar/times/')
    else:
        form = TimeForm()
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Editar
@login_required
def timeEditar(request, id):
    aba = 'Time'
    titulo = 'Editar Time'
    time = get_object_or_404(Time, pk=id)
    form = TimeForm(instance=time)

    if (request.method == 'POST'):
        form = TimeForm(request.POST, instance=time)
        if(form.is_valid()):
            time.save()
            messages.info(request, 'Cadastro editado com sucesso.')
            return redirect('/listar/times/')
        else:
            return render(request, 'cadastros/form.html', {'form': form, 'time': time})    
    else:
        return render(request, 'cadastros/form.html', {'form': form, 'titulo': titulo, 'aba': aba})


# Deletar
@login_required
def timeDeletar(request, id):
    time = get_object_or_404(Time, pk=id)
    busca_time = Jogo.objects.filter(time=id)

    if busca_time:
        messages.warning(request, f'O time {time.nome} não pode ser deletado pois já está cadastrado em Jogos!')
    else:
        time.delete()
        messages.warning(request, 'Time deletado com sucesso.')
 
    return redirect('/listar/times/')