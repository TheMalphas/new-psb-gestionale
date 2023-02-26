# Generated by Django 4.1 on 2023-02-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_addincforf_addrimborsi_addtrasferte_cedolini'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id_lista', models.BigAutoField(primary_key=True, serialize=False)),
                ('todo', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('fatta', models.IntegerField(blank=True, null=True)),
                ('setter', models.IntegerField(blank=True, null=True)),
                ('gruppo', models.IntegerField(blank=True, null=True)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'todo_list',
                'managed': False,
            },
        ),
    ]