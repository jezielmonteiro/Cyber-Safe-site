# Generated by Django 5.2 on 2025-05-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
    ]
