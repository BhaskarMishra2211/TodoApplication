from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TaskForm,NewUserForm,AssignForm,AssignTaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home_view(request):
    current_user = request.user
    todos = Todo.objects.filter(name = current_user)
    todos_count = Todo.objects.filter(name = current_user).all().count()
    completed_task = Todo.objects.filter(name = current_user,completed = True).count()

    context = {
        'todos':todos,
        'todos_count':todos_count,
        'completed_task':completed_task,
    }
    return render(request,'todo/todo_list.html',context = context)


@login_required
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.name = str(request.user) #because it is a usermodel #name is char filed
            task = form.save()
            task.save()
            messages.success(request,"Task added successfully ")
            return redirect('/',pk = task.pk)
    else:
        form = TaskForm()
    return render(request,'todo/create_todo.html',{'form':form})


def assign_task(request):
    if request.method == "POST":
        form = AssignTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AssignTaskForm()
    return render(request,'todo/assigntask.html',{'form':form})


@login_required
def editTask(request,pk):
    todo = get_object_or_404(Todo,pk = pk)
    if request.method == "POST":
        form = TaskForm(request.POST,instance = todo)
        if form.is_valid():
            todo = form.save()
            todo.save()
            return redirect('/',pk = todo.pk)
    else:
        form = TaskForm(instance = todo)
    return render(request,'todo/edit_todo.html',{'form':form})

@login_required
def todo_remove(request,pk):
    todo = get_object_or_404(Todo,pk = pk)
    todo.delete() # ,delete can delete any model inside tdjango
    return redirect('/')


@login_required
def get_allUsers(request):
    users = User.objects.all()
    return render(request,'todo/user_list.html',{'users':users})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration Successfull")
            return redirect("/")
        messages.error(request,"Something went wrong")
    else:
        form = NewUserForm()
    return render(request,'registration/Register.html',context={"register_form":form})

