# view.py
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    
    return render(request, 'new.html', { 'fulltext' : full_text ,'wordlist': word_list } )