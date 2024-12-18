# Generated by Django 5.1.3 on 2024-12-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockList', '0002_alter_tables_codprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='calificacion',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tables',
            name='codProd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tables',
            name='nomProd',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='tables',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tables',
            name='tipoProd',
            field=models.TextField(choices=[('Original', 'Original'), ('Marca alterna', 'Marca alterna')], max_length=13),
        ),
    ]
