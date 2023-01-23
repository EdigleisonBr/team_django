from django.urls import path
from .views.atleta import atletaListar, atletaCriar, atletaEditar, atletaDeletar
from .views.arbitro import arbitroListar, arbitroCriar, arbitroEditar, arbitroDeletar
from .views.local import localListar, localCriar, localEditar, localDeletar
from .views.time import timeListar, timeCriar, timeEditar, timeDeletar
from .views.jogo import jogoListar, jogoCriar, jogoEditar, jogoDeletar
from .views.gol import golListar, golCriar, golEditar, golDeletar, golMostrar, golsCadastrar


urlpatterns = [

    # Atleta
    path('listar/atletas/', atletaListar, name='listar-atletas'),
    path('cadastrar/atleta/', atletaCriar, name='cadastrar-atleta'),
    path('editar/atleta/<int:id>/', atletaEditar, name='editar-atleta'),
    path('excluir/atleta/<int:id>/', atletaDeletar, name='deletar-atleta'),

    # Arbitro
    path('listar/arbitros/', arbitroListar, name='listar-arbitros'),
    path('cadastrar/arbitro/', arbitroCriar, name='cadastrar-arbitro'),
    path('editar/arbitro/<int:id>/', arbitroEditar, name='editar-arbitro'),
    path('excluir/arbitro/<int:id>/', arbitroDeletar, name='deletar-arbitro'),

    # Local
    path('listar/locais/', localListar, name='listar-locais'),
    path('cadastrar/local/', localCriar, name='cadastrar-local'),
    path('editar/local/<int:id>/', localEditar, name='editar-local'),
    path('excluir/local/<int:id>/', localDeletar, name='deletar-local'),

    # Time
    path('listar/times/', timeListar, name='listar-times'),
    path('cadastrar/time/', timeCriar, name='cadastrar-time'),
    path('editar/time/<int:id>/', timeEditar, name='editar-time'),
    path('excluir/time/<int:id>/', timeDeletar, name='deletar-time'),

    # Jogo
    path('listar/jogos/', jogoListar, name='listar-jogos'),
    path('cadastrar/jogo/', jogoCriar, name='cadastrar-jogo'),
    path('editar/jogo/<int:id>/', jogoEditar, name='editar-jogo'),
    path('excluir/jogo/<int:id>/', jogoDeletar, name='deletar-jogo'),

    # Gols
    path('listar/gols/', golListar, name='listar-gols'),
    path('cadastrar/gol/', golCriar, name='cadastrar-gol'),
    path('cadastrar/gols/<int:id>/', golsCadastrar, name='cadastrar-gols'),
    path('editar/gol/<int:id>/', golEditar, name='editar-gol'),
    path('excluir/gol/<int:id>/', golDeletar, name='deletar-gol'),
    path('mostrar/gols/<int:id>/', golMostrar, name='mostrar-gols'),
]
