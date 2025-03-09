<<<<<<< HEAD
# Generated by Django 4.2.7 on 2025-03-09 04:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 4.2.7 on 2025-03-08 01:54

import django.core.validators
from django.db import migrations, models
>>>>>>> d4edcb778130b88afc19c4edaaeb436b985c8af6


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tryout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'Nama Tryout harus memiliki minimal 2 karakter')], verbose_name='Nama Tryout')),
                ('subject', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'Subject Tryout harus memiliki minimal 2 karakter')], verbose_name='Topik')),
                ('maximum_score', models.IntegerField(validators=[django.core.validators.MinValueValidator(100, 'Minimal nilainya 100 lah pak')], verbose_name='Skor Maksimum')),
                ('quiz_author', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3, 'Nama pembuat soal harus memiliki minimal 2 karakter')], verbose_name='Pembuat Soal')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('question_count', models.IntegerField(default=0, verbose_name='Jumlah Soal')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Pertanyaan harus memiliki minimal 2 karakter')], verbose_name='Pertanyaan')),
                ('answer', models.BooleanField(verbose_name='Jawaban')),
                ('tryout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.tryout')),
=======
                ('name', models.CharField(help_text='contoh: Tryout UAS DDP2\n', max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character\n')])),
                ('subject', models.CharField(help_text='contoh: DDP2\n', max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
                ('maximum_score', models.IntegerField(validators=[django.core.validators.MinValueValidator(100, message='Minimal nilainya 100 lah pak')])),
>>>>>>> d4edcb778130b88afc19c4edaaeb436b985c8af6
            ],
        ),
    ]
