# Generated by Django 3.2.5 on 2023-02-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStraordinari',
            fields=[
                ('id_straordinari', models.BigAutoField(primary_key=True, serialize=False)),
                ('rel_giorno', models.DateField(blank=True, null=True)),
                ('rel_time', models.TimeField(blank=True, null=True)),
                ('stato', models.IntegerField(blank=True, null=True)),
                ('ore', models.FloatField(blank=True, null=True)),
                ('valore', models.FloatField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('timestamp_creazione', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Add_Straordinari',
                'managed': False,
            },
        ),
    ]
