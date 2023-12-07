from django.forms import ModelForm
from .models import Avtomobile

class AvtoForm(ModelForm):
    class Meta:
        model = Avtomobile
        fields = '__all__'