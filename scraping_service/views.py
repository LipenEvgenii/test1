from django.shortcuts import render
import datetime

def home(request):
    data=datetime.datetime.now().date() #генерирует дату и время
    name='Dave'
    _context={"data":data,"name":name}
    return render(request,'home.html',_context)

