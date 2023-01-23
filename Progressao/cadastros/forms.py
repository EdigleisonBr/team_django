from django import forms

from .models import Atleta, Arbitro, Local, Time, Jogo, Gol

# Atleta
class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ('nome', 'apelido', 'posicao', 'data_nascimento', 'endereco', 'celular',)

#Local
class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ('nome',)

# Arbitro
class ArbitroForm(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields = ('nome', 'apelido', 'celular',)

# Time
class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ('nome', 'responsavel', 'celular',)

# Jogo
class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ('data_partida', 'hora', 'time', 'gols_contra')

# Gol
class GolForm(forms.ModelForm):
    class Meta:
        model = Gol
        fields = ('jogo', 'atleta', 'gols',)

