# Generated by Django 4.1 on 2023-02-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppoggioVerificaQr',
            fields=[
                ('uuid_qr', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'appoggio_verifica_qr',
                'managed': False,
            },
        ),
    ]
