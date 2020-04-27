from django.shortcuts import render,redirect

from .models import todo

from django.contrib import messages
from .forms import TodoForm

def add(request):

    item_list = todo.objects.order_by("-date")
    if request.method == "POST":
        form  = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    context = {
        "forms": form,
        "list":item_list,
        "title":"TODO LIST",
    }

    return render(request, 'todo/index.html',context)

def remove(request, item_id):
    item = todo.objects.get(id=item_id)
    item.delete()
    messages.info(request , "item removed succesfully!!!")
    return redirect('todo')
