# Generated by Django 3.2.9 on 2021-11-29 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcompanhamentoComposteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_acomp', models.DateField(blank=True, null=True)),
                ('moscas', models.BooleanField(blank=True, null=True)),
                ('minhocas_morte', models.BooleanField(blank=True, null=True)),
                ('temperatura', models.FloatField(blank=True, null=True)),
                ('muita_umidade', models.BooleanField(blank=True, null=True)),
                ('odor_desagradavel', models.BooleanField(blank=True, null=True)),
                ('pontuacao_acomp', models.IntegerField(blank=True, null=True)),
                ('img_acomp', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'AcompanhamentoComposteira',
            },
        ),
    ]
