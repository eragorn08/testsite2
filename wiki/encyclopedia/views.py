from django.shortcuts import render

from django.shortcuts import redirect

from django.core.files.storage import default_storage

from django.core.files.base import ContentFile

import markdown2

import re

import random

from . import util

from .forms import New_Title, New_Content


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    success = True
    if request.method == "POST":
        form0 = New_Title(request.POST)
        form1 = New_Content(request.POST)
        if form0.is_valid() and form1.is_valid():
            title = form0.cleaned_data["title"]
            content = form1.cleaned_data["content"]
            for entry in util.list_entries():
                if title.lower() == entry.lower():
                    success = False
                    return render(request,"encyclopedia/add.html",{
                        "success":success,
                        "formtitle":New_Title(),
                        "formcontent":New_Content()
                    })
            filename = f"entries/{title}.md"
            default_storage.save(filename, ContentFile(content))
            return redirect('entry_page',title)
        else:
            return render(request,"encyclopedia/add,html",{
                "success":success,
                "formtitle":title,
                "formcontent":content
            })
    else:
        return render(request,"encyclopedia/add.html",{
                        "success":success,
                        "formtitle":New_Title(),
                        "formcontent":New_Content()
                    })

def entry_page(request,name):
    if util.get_entry(name) == None:
        return render(request,"encyclopedia/404.html",context)
    else:
        output = markdown2.markdown(util.get_entry(name))
        return render(request, "encyclopedia/entry.html", {
            "content":output,"title":name.capitalize()
        })

def search(request):
    listEntry = util.list_entries()
    query = request.GET.get('q',None)
    query = query.lower()
    if util.get_entry(query):
        return redirect('entry_page', query)
    else:
        list_match = []
        for files in listEntry:
            filename =  files
            files = files.lower()
            for i in range(len(files)):
                if files[i:i+len(query)] == query:
                    list_match += [filename]
                else:
                    break
        return render (request, "encyclopedia/search.html",{
            "query":query,
            "entries":list_match
        })

def edit_page(request,title):
    content = util.get_entry(title)
    if request.method == "POST":
        content = request.POST.get("content","")
        util.save_entry(title,content)
        return redirect('entry_page', title)
    else:
        return render(request, "encyclopedia/edit.html",{
            "save_title":title,
            "save_markdown":content
        })

def random_page(request):
    selected_page = random.choice(util.list_entries())
    return redirect('entry_page', selected_page)