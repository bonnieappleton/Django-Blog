from django.shortcuts import render
from .models import ListItem

def shopping_list(request):
    list_items = ListItem.objects.filter(displayed=True)
    return render(request, 'shoppinglist/shopping_list.html', {'list_items': list_items})
