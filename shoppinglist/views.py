from django.shortcuts import render
from .models import ListItem

def shopping_list(request):
    list_items = ListItem.objects.filter(displayed=True)
    return render(request, 'shoppinglist/shopping_list.html', {'list_items': list_items})

def add_item(request):
    if request.method == "POST":
        form = ShoppingForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.displayed = True
            item.save()
    else:
        form = ShoppingForm()
    return render(request, 'shoppinglist/shopping_list.html', {'list_items': list_items})
