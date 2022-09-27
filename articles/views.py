from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name":'족발',"price":30000}, 
             {"name":'치킨', "price":25000}, 
             {"name":'마라탕', "price":15000}, 
             {"name":'떡볶이', "price":5000}, 
             {"name":'부대찌개', "price":20000}]
    pick = random.choice(menus)
    context = {
        'pick':pick,
        'name':name,
        'menus':menus,
    }
    return render(request, 'dinner.html', context)