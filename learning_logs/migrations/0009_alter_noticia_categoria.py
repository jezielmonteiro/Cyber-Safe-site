# Generated by Django 5.2 on 2025-05-29 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0008_alter_noticia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(choices=[('Vulnerabilidades', 'Vulnerabilidades'), ('Ameaças', 'Ameaças'), ('Tendências', 'Tendências'), ('Cibersegurança', 'Cibersegurança em geral')], max_length=100),
        ),
    ]
