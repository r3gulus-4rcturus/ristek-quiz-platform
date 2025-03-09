from django.forms import ModelForm
from quizapp.models import *

class MakeTryout(ModelForm):
    class Meta:
        model = Tryout
        fields = '__all__'
        # question count akan otomatis di set saat user menambahkan soal
        # jadi tidak perlu meminta kepada user berapa jumlah soal 
        exclude = ['question_count']   

class MakeQuestion(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['tryout']