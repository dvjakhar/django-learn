from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext=request.GET['text']

    list = fulltext.split()

    worddictionary = {}
    for word in list:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    return render(request, 'count.html',{'fulltext':fulltext,'countz':len(list),'worddictionary':worddictionary.items})

def about(request):
    return render(request, 'about.html')
