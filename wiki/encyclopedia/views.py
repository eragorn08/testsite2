from django import forms
from django.shortcuts import render

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    entry = forms.CharField(label="New Entry")
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,name):
    
    return render(request, "encyclopedia/page.html", {
        "title": name.capitalize()
    })

def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        save_entry(form.title,form.entry)
        return render(request,"encyclopedia/add.html",{
        "form": form})
    else:
        return render(request,"encyclopedia/add.html",{
        "form": NewEntryForm()
    })
    

    


