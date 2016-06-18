from django.shortcuts import render
from .models import ListItem
from .forms import ShoppingForm
import logging

logger = logging.getLogger(__name__)

def shopping_list(request):
    logger.error('I am rendering the page')
    if request.method == "POST":
        logger.error(request.POST)
        if 'name' in request.POST:
            add_item(request)
        elif 'delete' in request.POST:
            logger.error("I am deleting an item")
            delete_item(request)
        elif 'save' in request.POST:
            logger.error("I am dealing with the checkboxes")
            checkboxes(request)
        else:
            logger.error("Error!")
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

def delete_item(request):
    #Get value of delete from request.POST
    item_id = request.POST['delete']
    logger.error('id is ' + item_id)
    #Update the object with that id to make displayed = False and checked = False
    ListItem.objects.filter(id=item_id).update(displayed=False, checked=False)

def checkboxes(request):
    #Get value of checkboxes from request.POST
    item_ids_list = request.POST.getlist('list-item')
    #Update all displayed objects to be checked=False
    ListItem.objects.filter(displayed=True).update(checked=False)
    #Update displayed objects with values as ids to be checked=True
    for item_id in item_ids_list:
        logger.error('id: ' + item_id)
        ListItem.objects.filter(id=item_id).update(checked=True)
