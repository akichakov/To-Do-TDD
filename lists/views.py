from django.shortcuts import render, redirect
from .models import Item, List


def home_page(request):
    """Создать домашнюю страницу."""
    return render(request, 'home.html')


def view_list(request, list_id):
    """Создать представление списка."""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    """Создать новый список."""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    """Добавить элемент."""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
