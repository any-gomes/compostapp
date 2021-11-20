# Generated by Django 3.2.8 on 2021-11-20 21:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desempenhoMeta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_meta', models.IntegerField(verbose_name=django.db.models.fields.UUIDField)),
                ('nome', models.CharField(max_length=50)),
                ('data_inicio_meta', models.DateField()),
                ('data_fim_meta', models.DateField()),
                ('concluida', models.BooleanField()),
                ('desempenhoMeta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='desempenhoMeta.desempenhometa')),
            ],
            options={
                'db_table': 'Meta',
            },
        ),
    ]