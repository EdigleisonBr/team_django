# Generated by Django 3.2.16 on 2022-11-08 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('apelido', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apelido')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Celular')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('apelido', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apelido')),
                ('posicao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Posição')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Celular')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('responsavel', models.CharField(blank=True, max_length=255, null=True, verbose_name='Responsável')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Celular')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_partida', models.DateField(verbose_name='Data do jogo')),
                ('hora', models.CharField(max_length=6, verbose_name='Hora do jogo')),
                ('gols_contra', models.IntegerField(blank=True, null=True, verbose_name='Gols contra')),
                ('gols_favor', models.IntegerField(blank=True, null=True, verbose_name='Gols a favor')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('arbitro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.arbitro', verbose_name='Árbitro')),
                ('local', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.local', verbose_name='Local')),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.time', verbose_name='Time Adversário')),
            ],
        ),
        migrations.CreateModel(
            name='Gol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gols', models.IntegerField(verbose_name='Gols')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.atleta', verbose_name='Jogador')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.jogo', verbose_name='Jogo')),
            ],
        ),
    ]
