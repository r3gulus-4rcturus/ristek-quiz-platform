from django.forms import ModelForm
from quizapp.models import Tryout

class MakeTryout(ModelForm):
    class Meta:
        model = Tryout
        fields = '__all__'