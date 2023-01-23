from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Este decoretor obriga o usuário estar registrado para entrar em determinada função.

from ..models import Jogo, Gol
from ..forms import JogoForm
from django.db.models import Count

# Listar
@login_required
def jogoListar(request):
    jogos = Jogo.objects.all().order_by('data_partida')

    ## JANEIRO ############################################################
    # Contador de Jogos do mês
    jan = Jogo.objects.filter(data_partida__month=1).aggregate(Count('id'))
    jan_vazio = True
    if jan['id__count'] == 0:
        jan_vazio = False

    # (jogo_jan) - Ids dos jogos de Janeiro
    id_jogos_jan = Jogo.objects.filter(data_partida__month=1)
    jogo_jan = [] # lista de ids dos jogos
    for key in id_jogos_jan:
        jogo_jan.append(key.id)
    
    # Lista de Atletas/Gols de Janeiro
    gol_atleta_jan = []
    atleta_gols_jan ={}
    for ids in jogo_jan:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_jan['id'] = a.jogo.id
            atleta_gols_jan['nome'] = a.atleta.nome
            atleta_gols_jan['gols'] = a.gols
            gol_atleta_jan.append(atleta_gols_jan.copy())
    

    ## FEVEREIRO ############################################################
    # Contador de Jogos do mês
    fev = Jogo.objects.filter(data_partida__month=2).aggregate(Count('id'))
    fev_vazio = True
    if fev['id__count'] == 0:
        fev_vazio = False
    
    # (jogo_fev) - Ids dos jogos de Fevereiro
    id_jogos_fev = Jogo.objects.filter(data_partida__month=2)
    jogo_fev = [] # lista de ids dos jogos
    for key in id_jogos_fev:
        jogo_fev.append(key.id)

    # Lista de Atletas/Gols de Fevereiro
    gol_atleta_fev = []
    atleta_gols_fev ={}
    
    for ids in jogo_fev:
    
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_fev['id'] = a.jogo.id
            atleta_gols_fev['nome'] = a.atleta.nome
            atleta_gols_fev['gols'] = a.gols
            gol_atleta_fev.append(atleta_gols_fev.copy())
    
    
    ## MARÇO ############################################################
    # Contador de Jogos do mês
    mar = Jogo.objects.filter(data_partida__month=3).aggregate(Count('id'))
    mar_vazio = True
    if mar['id__count'] == 0:
        mar_vazio = False
    
    # (jogo_mar) - Ids dos jogos de Março
    id_jogos_mar = Jogo.objects.filter(data_partida__month=3)
    jogo_mar = [] # lista de ids dos jogos
    for key in id_jogos_mar:
        jogo_mar.append(key.id)

    # Lista de Atletas/Gols de Março
    gol_atleta_mar = []
    atleta_gols_mar ={}
    for ids in jogo_mar:
        
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_mar['id'] = a.jogo.id
            atleta_gols_mar['nome'] = a.atleta.nome
            atleta_gols_mar['gols'] = a.gols
            gol_atleta_mar.append(atleta_gols_mar.copy())
    
    
    ## Abril ############################################################
    # Contador de Jogos do mês
    abr = Jogo.objects.filter(data_partida__month=4).aggregate(Count('id'))
    abr_vazio = True
    if abr['id__count'] == 0:
        abr_vazio = False
    
    # (jogo_abr) - Ids dos jogos
    id_jogos_abr = Jogo.objects.filter(data_partida__month=4)
    jogo_abr = [] # lista de ids dos jogos
    for key in id_jogos_abr:
        jogo_abr.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_abr = []
    atleta_gols_abr ={}
    for ids in jogo_abr:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_abr['id'] = a.jogo.id
            atleta_gols_abr['nome'] = a.atleta.nome
            atleta_gols_abr['gols'] = a.gols
            gol_atleta_abr.append(atleta_gols_abr.copy())
    
    
    ## Maio ############################################################
    # Contador de Jogos do mês
    mai = Jogo.objects.filter(data_partida__month=5).aggregate(Count('id'))
    mai_vazio = True
    if mai['id__count'] == 0:
        mai_vazio = False
    
    # (jogo_mai) - Ids dos jogos
    id_jogos_mai = Jogo.objects.filter(data_partida__month=5)
    jogo_mai = [] # lista de ids dos jogos
    for key in id_jogos_mai:
        jogo_mai.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_mai = []
    atleta_gols_mai ={}
    for ids in jogo_mai:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_mai['id'] = a.jogo.id
            atleta_gols_mai['nome'] = a.atleta.nome
            atleta_gols_mai['gols'] = a.gols
            gol_atleta_mai.append(atleta_gols_mai.copy())
    
    ## Junho ############################################################
    # Contador de Jogos do mês
    jun = Jogo.objects.filter(data_partida__month=6).aggregate(Count('id'))
    jun_vazio = True
    if jun['id__count'] == 0:
        jun_vazio = False
    
    # (jogo_jun) - Ids dos jogos
    id_jogos_jun = Jogo.objects.filter(data_partida__month=6)
    jogo_jun = [] # lista de ids dos jogos
    for key in id_jogos_jun:
        jogo_jun.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_jun = []
    atleta_gols_jun ={}
    for ids in jogo_jun:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_jun['id'] = a.jogo.id
            atleta_gols_jun['nome'] = a.atleta.nome
            atleta_gols_jun['gols'] = a.gols
            gol_atleta_jun.append(atleta_gols_jun.copy())


    ## Julho ############################################################
    # Contador de Jogos do mês 
    jul = Jogo.objects.filter(data_partida__month=7).aggregate(Count('id'))
    jul_vazio = True
    if jul['id__count'] == 0:
        jul_vazio = False

    # (jogo_jul) - Ids dos jogos
    id_jogos_jul = Jogo.objects.filter(data_partida__month=7)
    jogo_jul = [] # lista de ids dos jogos
    for key in id_jogos_jul:
        jogo_jul.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_jul = []
    atleta_gols_jul ={}
    
    for ids in jogo_jul:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_jul['id'] = a.jogo.id
            atleta_gols_jul['nome'] = a.atleta.nome
            atleta_gols_jul['gols'] = a.gols
            gol_atleta_jul.append(atleta_gols_jul.copy())


    ## Agosto ############################################################
    # Contador de Jogos do mês
    ago = Jogo.objects.filter(data_partida__month=8).aggregate(Count('id'))
    ago_vazio = True
    if ago['id__count'] == 0:
        ago_vazio = False
    
    # (jogo_ago) - Ids dos jogos
    id_jogos_ago = Jogo.objects.filter(data_partida__month=8)
    jogo_ago = [] # lista de ids dos jogos
    for key in id_jogos_ago:
        jogo_ago.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_ago = []
    atleta_gols_ago ={}
    
    for ids in jogo_ago:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_ago['id'] = a.jogo.id
            atleta_gols_ago['nome'] = a.atleta.nome
            atleta_gols_ago['gols'] = a.gols
            gol_atleta_ago.append(atleta_gols_ago.copy())


    ## Setembro ############################################################
    # Contador de Jogos do mês
    set = Jogo.objects.filter(data_partida__month=9).aggregate(Count('id'))
    set_vazio = True
    if set['id__count'] == 0:
        set_vazio = False
    
    # (jogo_set) - Ids dos jogos
    id_jogos_set = Jogo.objects.filter(data_partida__month=9)
    jogo_set = [] # lista de ids dos jogos
    for key in id_jogos_set:
        jogo_set.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_set = []
    atleta_gols_set ={}
    
    for ids in jogo_set:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_set['id'] = a.jogo.id
            atleta_gols_set['nome'] = a.atleta.nome
            atleta_gols_set['gols'] = a.gols
            gol_atleta_set.append(atleta_gols_set.copy())


    ## Outubro ############################################################
    # Contador de Jogos do mês
    out = Jogo.objects.filter(data_partida__month=10).aggregate(Count('id'))
    out_vazio = True
    if out['id__count'] == 0:
        out_vazio = False
    
    # (jogo_out) - Ids dos jogos
    id_jogos_out = Jogo.objects.filter(data_partida__month=10)
    jogo_out = [] # lista de ids dos jogos
    for key in id_jogos_out:
        jogo_out.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_out = []
    atleta_gols_out ={}
    
    for ids in jogo_out:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_out['id'] = a.jogo.id
            atleta_gols_out['nome'] = a.atleta.nome
            atleta_gols_out['gols'] = a.gols
            gol_atleta_out.append(atleta_gols_out.copy())


    ## Novembro ############################################################
    # Contador de Jogos do mês
    nov = Jogo.objects.filter(data_partida__month=11).aggregate(Count('id'))
    nov_vazio = True
    if nov['id__count'] == 0:
        nov_vazio = False
    
    # (jogo_nov) - Ids dos jogos
    id_jogos_nov = Jogo.objects.filter(data_partida__month=11)
    jogo_nov = [] # lista de ids dos jogos
    for key in id_jogos_nov:
        jogo_nov.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_nov = []
    atleta_gols_nov ={}
    
    for ids in jogo_nov:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_nov['id'] = a.jogo.id
            atleta_gols_nov['nome'] = a.atleta.nome
            atleta_gols_nov['gols'] = a.gols
            gol_atleta_nov.append(atleta_gols_nov.copy())


    ## Dezembro ############################################################
    # Contador de Jogos do mês
    dez = Jogo.objects.filter(data_partida__month=12).aggregate(Count('id'))
    dez_vazio = True
    if dez['id__count'] == 0:
        dez_vazio = False

    # (jogo_dez) - Ids dos jogos
    id_jogos_dez = Jogo.objects.filter(data_partida__month=11)
    jogo_dez = [] # lista de ids dos jogos
    for key in id_jogos_dez:
        jogo_dez.append(key.id)

    # Lista de Atletas/Gols
    gol_atleta_dez = []
    atleta_gols_dez ={}
    
    for ids in jogo_dez:
        gols_jogo = Gol.objects.filter(jogo=ids)
        for a in gols_jogo:
            atleta_gols_dez['id'] = a.jogo.id
            atleta_gols_dez['nome'] = a.atleta.nome
            atleta_gols_dez['gols'] = a.gols
            gol_atleta_dez.append(atleta_gols_dez.copy())

    # paginator = Paginator(tasks_list, 6) # (Lista das tarefas, nº de exibição por página).
    # page = request.GET.get('page') # Resgata o argumento page do Request.
    # tasks = paginator.get_page(page) # Exibe os elementos da página correta. 

    return render(request, 'cadastros/jogo/listar.html', { 
        'jogos': jogos, 
        'jan_vazio': jan_vazio,
        'gol_atleta_jan': gol_atleta_jan,
        'fev_vazio': fev_vazio,
        'gol_atleta_fev': gol_atleta_fev,
        'mar_vazio': mar_vazio,
        'gol_atleta_mar': gol_atleta_mar,
        'abr_vazio': abr_vazio,
        'gol_atleta_abr': gol_atleta_abr,
        'mai_vazio': mai_vazio,
        'gol_atleta_mai': gol_atleta_mai,
        'jun_vazio': jun_vazio,
        'gol_atleta_jun': gol_atleta_jun,
        'jul_vazio': jul_vazio,
        'gol_atleta_jul': gol_atleta_jul,
        'ago_vazio': ago_vazio,
        'gol_atleta_ago': gol_atleta_ago,
        'set_vazio': set_vazio,
        'gol_atleta_set': gol_atleta_set,
        'out_vazio': out_vazio,
        'gol_atleta_out': gol_atleta_out,
        'nov_vazio': nov_vazio,
        'gol_atleta_nov': gol_atleta_nov,
        'dez_vazio': dez_vazio,
        'gol_atleta_dez': gol_atleta_dez,
    })

# Criar
@login_required
def jogoCriar(request):
    aba = 'Jogo'
    titulo = 'Cadastrar Jogo'
    if request.method == 'POST':
        form = JogoForm(request.POST)
                                        
        if form.is_valid():
            jogo = form.save(commit=False) # (commit=False) para o processo de salvamento para executar a linha de baixo.
            jogo.save()
            messages.success(request, 'Cadastro salvo com sucesso.')
            return redirect('/listar/jogos/')
    else:
        form = JogoForm()
        return render(request, 'cadastros/form.html', {'form': form, 'aba': aba, 'titulo': titulo})


# Editar
@login_required
def jogoEditar(request, id):
    aba = 'Jogo'
    titulo = 'Editar Jogo'
    jogo = get_object_or_404(Jogo, pk=id)
    form = JogoForm(instance=jogo)

    if (request.method == 'POST'):
        form = JogoForm(request.POST, instance=jogo)
        if(form.is_valid()):
            jogo.save()
            messages.info(request, 'Cadastro editado com sucesso.')
            return redirect('/listar/jogos/')
        else:
            return render(request, 'cadastros/form.html', {'form': form, 'jogo': jogo})    
    else:
        return render(request, 'cadastros/form.html', {'form': form, 'aba': aba, 'titulo': titulo})


# Deletar
@login_required
def jogoDeletar(request, id):
    jogo = get_object_or_404(Jogo, pk=id)

    #Excluir os gols vinculados ao Jogo
    gols = Gol.objects.filter(jogo=id)
    gols.delete()
    jogo.delete()

    messages.warning(request, 'Jogo e gols deletados com sucesso.')

    return redirect('/listar/jogos/')