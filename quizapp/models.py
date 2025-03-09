from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

# Tryout Models
class Tryout(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Nama Tryout",
        validators=[MinLengthValidator(2, "Nama Tryout harus memiliki minimal 2 karakter")]
    )
    subject = models.CharField(
        max_length=30,
        verbose_name="Topik",
        validators=[MinLengthValidator(2, "Subject Tryout harus memiliki minimal 2 karakter")]
    )
    maximum_score = models.IntegerField(
        verbose_name="Skor Maksimum",
        validators=[MinValueValidator(100, "Minimal nilainya 100 lah pak")]
    )
    quiz_author = models.CharField(
        max_length=30,
        verbose_name="Pembuat Soal",
        validators=[MinLengthValidator(3, "Nama pembuat soal harus memiliki minimal 2 karakter")]
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    question_count = models.IntegerField(
        verbose_name="Jumlah Soal",
        default=0
    )

    def __str__(self) :
        return self.name

# Question Models
class Question(models.Model):
    question_text = models.CharField(
        max_length=100,
        verbose_name="Pertanyaan",
        validators=[MinLengthValidator(2, "Pertanyaan harus memiliki minimal 2 karakter")]
    )
    answer = models.BooleanField(
        verbose_name="Jawaban"
    )
    tryout = models.ForeignKey(
        to=Tryout, 
        null=True,
        on_delete=models.CASCADE
    )