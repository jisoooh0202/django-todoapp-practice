from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


def todo_list(request):
	todos = Todo.objects.all()
	context = {
		"todo_list": todos
	}
	print(todos)
	return render(request, "todo_list.html", context)

# CRUD - Create, Retrieve, Update, Delete, List

def todo_detail(request, id):
	todo = Todo.objects.get(id=id)
	context = {
		"todo": todo
	}
	return render(request, "todo_detail.html", context)


def todo_create(request):
	form = TodoForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {"form": form}
	return render(request, "todo_create.html", context)
	