from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list', views.get_countries_list),
    path('name/<str:country>', views.get_country),
    path('about', views.about),
    path('item/<str:alpha>', views.get_alphabet),
    #path('name/<str:alpha>', views.get_alpha_country),
    #path('item/<int:id>', views.get_item),
    #path('items', views.item_list)
]
