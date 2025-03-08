from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

# Tryout Models
class Tryout(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="contoh: Tryout UAS DDP2",
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    subject = models.CharField(
        max_length=30,
        help_text="contoh: DDP2",
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    maximum_score = models.IntegerField(
        validators=[MinValueValidator(100, message="Minimal nilainya 100 lah pak")]
    )

# Question Models
# class Questions
