from django.shortcuts import render

def shopping_list(request):
    return render(request, 'shoppinglist/shopping_list.html', {})
