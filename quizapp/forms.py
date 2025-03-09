from django.forms import ModelForm
<<<<<<< HEAD
from quizapp.models import *
=======
from quizapp.models import Tryout
>>>>>>> d4edcb778130b88afc19c4edaaeb436b985c8af6

class MakeTryout(ModelForm):
    class Meta:
        model = Tryout
<<<<<<< HEAD
        fields = '__all__'
        # question count akan otomatis di set saat user menambahkan soal
        # jadi tidak perlu meminta kepada user berapa jumlah soal 
        exclude = ['question_count']   

class MakeQuestion(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['tryout']
=======
        fields = '__all__'
>>>>>>> d4edcb778130b88afc19c4edaaeb436b985c8af6
