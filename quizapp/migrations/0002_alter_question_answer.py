# Generated by Django 4.2.7 on 2025-03-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('', ''), ('Benar', 'Benar'), ('Salah', 'Salah')], max_length=10, verbose_name='Jawaban'),
        ),
    ]
