from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add/', views.add, name='add'),
  path('create_item/', views.CreateItem.as_view(), name='create_item'),
  path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
]

