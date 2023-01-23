from django.views.generic import TemplateView
from datetime import datetime 
from django.db.models import Sum, Max, Count

from cadastros.models import Jogo, Gol, Atleta

from operator import itemgetter

class PaginaInicial(TemplateView):
    template_name = "paginas/index.html"

    # Criar dados para mandar pro HTML
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        # Lista de jogos do mês
        context['data'] = datetime.now().month                                      # Pegando o mês atual
        context['mes'] = str(context['data'])                                       # Transformando em string para ser comparado
        context['jogos'] = Jogo.objects.filter(data_partida__month=context['mes'])  # Filtrando jogos de um determinado mês

        # Soma dos Gols a Favor
        gols_favor = Jogo.objects.all().aggregate(Sum('gols_favor'))
        context['gols_favor'] = gols_favor['gols_favor__sum']
        
        # Soma dos Gols Contra
        gols_contra = Jogo.objects.all().aggregate(Sum('gols_contra'))
        context['gols_contra'] = gols_contra['gols_contra__sum']  

        # Artilheiro
        gols_atletas = {}
        lista_artilheiros = []        

        # Total de gols por atleta ordenados em ordem decrescente
        gols = Gol.objects.values('atleta').annotate(num_gols=Sum('gols')).order_by('-num_gols')
        context['gols'] = gols
        
        # A partir da query acima salva o atleta e o id em um dicionário por order descrescente
        for g in gols:
            atleta = Atleta.objects.get(id=g['atleta'])
            gols_atletas['atleta'] = atleta.nome
            gols_atletas['gols'] = g['num_gols']
            lista_artilheiros.append(gols_atletas.copy())
        
        context['lista_artilheiros'] = lista_artilheiros
               
        return context 

  
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"