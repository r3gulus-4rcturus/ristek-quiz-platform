import django_filters  
from quizapp.models import Tryout

class TryoutFilter(django_filters.FilterSet):

    # Set beberapa filter dengan lookp_expr = contains untuk mencocokkan
    # ke data yang mengandung suatu string walaupun tidak tepat sama
    name_filter = django_filters.CharFilter(field_name="name", lookup_expr='contains')
    subject_filter = django_filters.CharFilter(field_name="subject", lookup_expr='contains')
    date_filter = django_filters.DateFilter(field_name="date_created", lookup_expr='contains')
    
    class Meta:
        model = Tryout
        fields = []


