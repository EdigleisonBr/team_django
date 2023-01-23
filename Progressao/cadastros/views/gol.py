from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Este decoretor obriga o usuário estar registrado para entrar em determinada função.

from ..models import Gol, Jogo, Atleta
from ..forms import GolForm
from django.db.models import Count


# Listar
@login_required
def golListar(request):

    gols = Gol.objects.all().order_by('id')
    
    gol_count = Gol.objects.all().aggregate(Count('id'))
    gol_vazio = True
    if gol_count['id__count'] == 0:
        gol_vazio = False

    # paginator = Paginator(tasks_list, 6) # (Lista das tarefas, nº de exibição por página).
    # page = request.GET.get('page') # Resgata o argumento page do Request.
    # tasks = paginator.get_page(page) # Exibe os elementos da página correta. 

    return render(request, 'cadastros/gol/listar.html', {'gols': gols, 'gol_vazio': gol_vazio})

# Criar (ANTIGO)
@login_required
def golsCadastrar(request, id):
    aba = 'Gol'
    titulo = 'Cadastrar Gol'
    jogo = get_object_or_404(Jogo, pk=id)
    atletas = Atleta.objects.all().order_by('nome')
       
    return render(request, 'cadastros/gol/cadastrar.html', {'time': jogo.time, 
                                                            'data': jogo.data_partida,
                                                            'titulo': titulo, 
                                                            'aba': aba,
                                                            'atletas': atletas,
                                                            'jogo': jogo.id,
                                                            })


# Criar
@login_required
def golCriar(request):
    
    ids = request.GET.get("arrayId")
    atletas = request.GET.get("arrayA")
    gols_atleta = request.GET.get('arrayG')
    id_jogo = request.GET.get('jogo_id')
    gols_contra = request.GET.get('gols_contra')

    if gols_atleta:
        array_atletas = atletas.split(',')
        array_ids = ids.split(',')
        array_gols = gols_atleta.split(',')

        # Somando gols dos atletas para salvar em Jogo
        gols_feitos = 0
        for g in array_gols:
            gols_feitos = gols_feitos + int(g)
        
        cont = len(array_atletas)

        # Salvando gols dos atletas
        jogo_id = Jogo.objects.get(id=id_jogo)
        for i in range(0, cont):
            atleta_id = Atleta.objects.get(id=array_ids[i])
            gols = Gol(jogo=jogo_id, atleta=atleta_id, gols=array_gols[i])
            gols.save()

        #Salvando gols Feitos no Jogo
        Jogo.objects.filter(id=jogo_id.id).update(gols_favor=gols_feitos)
    else:
        #Salvando gols Feitos no Jogo (0)
        jogo_id = Jogo.objects.get(id=id_jogo)
        Jogo.objects.filter(id=jogo_id.id).update(gols_favor=0) 

    if gols_contra:
        #Salvando gols contra Feitos no Jogo
        Jogo.objects.filter(id=jogo_id.id).update(gols_contra=gols_contra)
    else:
        Jogo.objects.filter(id=jogo_id.id).update(gols_contra=0)    

    messages.success(request, 'Gols cadastrados com sucesso.')
    return redirect('/listar/jogos/')
     

# Editar
@login_required
def golEditar(request, id):
    gol = get_object_or_404(Gol, pk=id)
    form = GolForm(instance=gol)

    if (request.method == 'POST'):
        form = GolForm(request.POST, instance=gol)
        if(form.is_valid()):
            gol.save()
            messages.info(request, 'Cadastro editado com sucesso.')
            return redirect('/listar/gols/')
        else:
            return render(request, 'cadastros/form.html', {'form': form, 'gol': gol})    
    else:
        return render(request, 'cadastros/form.html', {'form': form, 'gol': gol})


# Deletar
@login_required
def golDeletar(request, id):
    
    # Zerando gols no Jogo
    Jogo.objects.filter(id=id).update(gols_favor=None)
    
    #Deletando gols
    gol = Gol.objects.filter(jogo=id)
    gol.delete()

    messages.warning(request, 'Cadastro deletado com sucesso.')

    return redirect('/listar/jogos/')


# Editar
@login_required
def golMostrar(request, id):
    gols = Gol.objects.filter(jogo=id)
    teste = 'edigleison'
        
    return render(request, 'cadastros/gol/mostrar-gols.html', {'gols': gols, 'teste': teste})