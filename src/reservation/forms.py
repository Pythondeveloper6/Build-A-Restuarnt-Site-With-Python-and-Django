from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'