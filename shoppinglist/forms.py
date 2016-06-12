from django import forms
from .models import ListItem

class ShoppingForm(forms.MetaForm):
    class Meta:
        model = ListItem
        fields = ('name', 'section',)
