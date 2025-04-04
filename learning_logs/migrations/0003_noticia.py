# Generated by Django 5.1.6 on 2025-03-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.CharField(choices=[('vulnerabilidades', 'Vulnerabilidades'), ('ameaças', 'Ameaças'), ('tendencias', 'Tendências'), ('ciberseguranca', 'Cibersegurança em geral')], max_length=100)),
            ],
        ),
    ]
