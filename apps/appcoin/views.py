from django.shortcuts import render, redirect
from .models import Currency, AppCoin, DataDump
import httplib2
import json
# Create your views here.

def newpage(request):
    return render(request, "appcoin/new.html")

def index(request):
    # getDataDump()
    context = {
    "currency": Currency.currencyManager.all(),
    "appcoin": AppCoin.ACManager.all(),
    "datadump": DataDump.DDManager.all()
    }
    return render(request, "appcoin/index.html", context)

def getDataDump():
    h = httplib2.Http(".cache")
    resp, content = h.request("https://api.coinmarketcap.com/v1/ticker/?limit=10", "GET")
    json_data = json.loads(content)
    # print type(json_data)
    DataDump.DDManager.add(json_data)


def createCurrency(request):
    # actually create the entry in the db. send it to models.
    Currency.currencyManager.add(request.POST)
    return redirect('/')

def createAppCoin(request):
    AppCoin.ACManager.add(request.POST)
    return redirect('/')

def showCurrency(request, id):
    context = {
    "currency": Currency.currencyManager.get(id = id)
    }
    return render(request,'appcoin/showCurrency.html', context)

def showAppCoin(request, id):
    context = {
    "appcoin": AppCoin.ACManager.get(id = id)
    }
    return render(request,'appcoin/showAppCoin.html')
