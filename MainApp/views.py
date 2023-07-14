from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import numpy as np

author ={
    "name" : "Иван",
    "middle" : "Петрович",
    "surname" : "Иванов",
    "phone" : "8-926-600-01-02",
    "email" : "vasya@mail.ru"}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


countries = [
    {
        "country": "Aruba",
        "languages": [
            "Dutch",
            "English",
            "Papiamento",
            "Spanish"
        ]
    },
    {
        "country": "Afghanistan",
        "languages": [
            "Balochi",
            "Dari",
            "Pashto",
            "Turkmenian",
            "Uzbek"
        ]
    },
     {
        "country": "Belarus",
        "languages": [
            "Belorussian",
            "Polish",
            "Russian",
            "Ukrainian"
        ]
    },
    {
        "country": "Germany",
        "languages": [
            "German",
            "Greek",
            "Italian",
            "Polish",
            "Southern Slavic Languages",
            "Turkish"
        ]
    }
]

from itertools import groupby, chain
from operator import itemgetter

initials = []
list_countries=[]
k=len(countries)
for country in countries:
    initials.append(country['country'][0])
    list_countries.append(country['country'])
Alphab_List = sorted(set(initials))
list_countries_splits = np.array_split(list_countries, len(list_countries))
Countries_List = [list(grp) for _,grp in groupby(sorted(chain.from_iterable(list_countries_splits)), key=itemgetter(0))]
dictionary_countries = dict(zip(Alphab_List, Countries_List))
alphas = list(dictionary_countries.keys())
countr = list(dictionary_countries.values())

# Будет в виде: {'A': ['Afghanistan', 'Aruba'], 'B': ['Belarus'], 'G': ['Germany']}

def home(request):
   context = {
       "name": "Петров Николай Иванович",
       "email": "my_mail@mail.ru"
   }
   return render(request, "index.html", context)


def get_countries_list(request):
    context = {'countries': countries,
               'alphas':list(dictionary_countries.keys()),
               'countr':list(dictionary_countries.values()),}
    return render(request, "countries-list.html", context)


def get_country(request, country):
    for name in countries:
        if name['country'] == country:
            context = {
                'name': name
            }
            return render(request, "name-page.html", context)
    return HttpResponseNotFound(f'Name with country={country} not found')


def get_alphabet(request, alpha):
    for item in list(dictionary_countries.keys()):
        if item == alpha:
            context = {
                'val': list(dictionary_countries.values()),
            }
        return render(request, 'alphabet-test.html', context)


############

def about(request):
    result = f'''
        Имя: <b>{author["name"]}</b><br>
        Отчество: <b>{author["middle"]}</b><br>
        Фамилия: <b>{author["surname"]}</b><br>
        телефон: <b>{author["phone"]}</b><br>
        Email: <b>{author["email"]}</b><br>
        <a href='/'> Home </a>
        '''
    return HttpResponse(result)


def get_item(request, id):
    for item in items:
       if item['id'] == id:
        context = {
            'item': item
        }
        return render(request, "item-page.html", context)

    return HttpResponseNotFound(f'Item with id={id} not found')


def item_list(request):
    context = {
        "items": items
    }
    # Аргументы render: Запрос(request), Имя файла-шаблона, Контекст (чем заполняем)
    return render(request, "items-list.html", context)