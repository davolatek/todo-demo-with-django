from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Todo

# Create your views here.

def list_todo_items(request):
    context = {'todo_lists': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context)


def insert_todo_items(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/lists')


def delete_todo_items(request, todo_id):
    todo_to_delete = Todo.objects.get(id= todo_id)
    todo_to_delete.delete()
    return redirect("/todos/lists")