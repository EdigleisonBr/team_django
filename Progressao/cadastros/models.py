from django.db import models
from datetime import datetime


class Atleta(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    apelido = models.CharField(max_length=255, verbose_name='Apelido', blank=True, null=True)
    posicao = models.CharField(max_length=255, verbose_name='Posição', blank=True, null=True)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    endereco = models.CharField(max_length=255, verbose_name='Endereço', blank=True, null=True)
    celular = models.CharField(max_length=255, verbose_name='Celular', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    
    # def idade(self):
    #     hoje = datetime.now()
    #     return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return self.nome

       
class Local(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Arbitro(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    apelido = models.CharField(max_length=255, verbose_name='Apelido', blank=True, null=True)
    celular = models.CharField(max_length=255, verbose_name='Celular', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
        

class Time(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    responsavel = models.CharField(max_length=255, verbose_name='Responsável', blank=True, null=True)
    celular = models.CharField(max_length=255, verbose_name='Celular', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    data_partida = models.DateField(verbose_name='Data do jogo')
    hora = models.CharField(max_length=6, verbose_name='Hora do jogo')
    time = models.ForeignKey(Time, verbose_name='Time Adversário', on_delete=models.PROTECT, blank=True, null=True)
    arbitro = models.ForeignKey(Arbitro, verbose_name='Árbitro', on_delete=models.PROTECT, blank=True, null=True)
    local = models.ForeignKey(Local, verbose_name='Local', on_delete=models.PROTECT, blank=True, null=True)
    gols_contra = models.IntegerField(verbose_name='Gols contra', blank=True, null=True)
    gols_favor = models.IntegerField(verbose_name='Gols a favor', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        data_p = self.data_partida.strftime('%d/%m/%Y')
        return f'{data_p} - Nonô {self.gols_favor} X {self.gols_contra} {self.time.nome}'
    
       

class Gol(models.Model):
    jogo = models.ForeignKey(Jogo, verbose_name='Jogo', on_delete=models.PROTECT)
    atleta = models.ForeignKey(Atleta, verbose_name='Jogador', on_delete=models.PROTECT)
    gols = models.IntegerField(verbose_name='Gols')
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        data_p = self.jogo.data_partida.strftime('%d/%m/%Y')
        return f'Data: {data_p} - Nonô {self.jogo.gols_favor} X {self.jogo.gols_contra} {self.jogo.time.nome}'


        


        

