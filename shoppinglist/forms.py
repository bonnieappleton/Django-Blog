from django import forms
from .models import ListItem

class ShoppingForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ('name', 'section',)
