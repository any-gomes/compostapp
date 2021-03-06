# Generated by Django 3.2.9 on 2021-11-29 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meta', '0001_initial'),
        ('acompanhamentoComposteira', '0001_initial'),
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data_inicio_comp', models.DateField(auto_now_add=True, null=True)),
                ('tamanho_comp', models.IntegerField(blank=True, null=True)),
                ('total_humus_produzido', models.FloatField(blank=True, null=True)),
                ('concluido', models.BooleanField(blank=True, null=True)),
                ('data_conclusao_comp', models.DateField(blank=True, null=True)),
                ('qualidade', models.BooleanField(blank=True, null=True)),
                ('humus_produzido', models.BooleanField(blank=True, null=True)),
                ('acompanhamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acompanhamentoComposteira.acompanhamentocomposteira')),
                ('insumo', models.ManyToManyField(to='insumo.Insumo', verbose_name='Lista de Insumos')),
                ('meta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meta.meta')),
            ],
            options={
                'db_table': 'Composteira',
            },
        ),
    ]
