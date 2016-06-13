from django.shortcuts import render
from .models import ListItem
from .forms import ShoppingForm
import logging

logger = logging.getLogger(__name__)

def shopping_list(request):
    logger.error('I am rendering the page')
    if request.method == "POST":
        add_item(request)
    list_items = ListItem.objects.filter(displayed=True)
    return render(request, 'shoppinglist/shopping_list.html', {'list_items': list_items})

def add_item(request):
    form = ShoppingForm(request.POST)
    print ('I am adding an item')
    logger.error(request.POST)
    if form.is_valid():
        logger.error('form is valid')
        item = form.save(commit=False)
        item.displayed = True
        item.save()
    else:
        logger.error('not valid')
        logger.error(form.errors)
