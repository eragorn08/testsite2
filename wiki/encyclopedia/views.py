from django import forms
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from . import util

class NewEntryTitle(forms.Form):
    title = forms.CharField(label="")
    
    

class NewEntry(forms.Form):
    entry = forms.CharField(widget=forms.Textarea,label="")
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,name):
    
    return render(request, "encyclopedia/page.html", {
        "title": name.capitalize()
    })

def add(request):
    if request.method == 'POST':
        form0 = NewEntryTitle(request.POST)
        form1 = NewEntry(request.POST)
        #title = form0.cleaned_data["title"]
        #entry = form1.cleaned_data["entry"]
        util.save_entry(form0,form1)
        return HttpResponseRedirect(reverse("encyclopedia/index.html"))
    else:
        return render(request,"encyclopedia/add.html", {
        "form_title":NewEntryTitle(),
        "form_entry":NewEntry()
        })
    
    

    


