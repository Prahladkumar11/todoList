from django.shortcuts import render,redirect,HttpResponse

from .models import *

def home(request):
    data=Todolist.objects.all()
    return render(request, 'todo_list.html',{"data":data})

def additem_page(request,id):
    data=Todolist.objects.all()
    selected=Todolist.objects.get(id=id)
    return render(request, 'addform.html',{"data":data,"selected":selected})


def addList(request):
    if request.method == 'POST':
        Title=request.POST.get('title')
        if Title:
            Todolist.objects.create(list_title=Title)
            return redirect('todo_list')
        else:
            return HttpResponse('<script> alert("not added")</script>')
    else:
        return HttpResponse('<script> alert("notsdf added")</script>')
    
def todo_item_page(request,id):
    list=Todolist.objects.get(id=id)
    item=ToDoItem.objects.filter(list=list)
    return render(request,'todo_item.html',{'item':item, 'list':list})
    
def delete_list(request,id):
    item=Todolist.objects.get(id=id)
    item.delete()
    return redirect('todo_list') 
    
    
    
def add_todo(request):
    if request.method == 'POST':
        list_id=request.POST.get('list_title')
        todolist=Todolist.objects.get(id=list_id)
        title=request.POST.get('title')
        due_date=request.POST.get('due_date')
        
        
        ToDoItem.objects.create(list=todolist,title=title,due_date=due_date)
        
        # list=Todolist.objects.get(id=list_id)
        # item=ToDoItem.objects.filter(list=list)
        # return render(request,'todo_item.html',{'item':item, 'list':list})
            
        return redirect('todoitem',list_id)
    
def delete_todo(request,id):
    item=ToDoItem.objects.get(id=id)
    item.delete()
    return redirect('todoitem',item.list.id)