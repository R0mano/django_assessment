from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Item

# Create your views here.
def home(request):
  items = Item.objects.all()
  return render(request, 'home.html', {'items': items})

def add(request):
  return render(request, 'add.html')

class CreateItem(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/'

def delete_item(request, item_id):
  item =Item.objects.get(id=item_id)
  item.delete()
  return redirect('home')
