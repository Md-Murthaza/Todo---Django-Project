from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view_tasks(request):
    todos = Todo.objects.all()
    return render(request,'view_tasks.html',{'todos':todos})

@login_required
def add_task(request):
    if request.method == "POST":
        todo_title  = request.POST.get('todo_title')
        todo_description = request.POST.get('todo_description')

        if todo_title:  # Check if title is not empty
            Todo.objects.create(todo_title=todo_title, todo_description=todo_description)
            print("Task added:", todo_title)
            return redirect('view_tasks')
        else:
            print("Todo title is empty!") 
    
    return render(request, 'add_task.html',{'request':request})

@login_required
def edit_task(request,task_id):
    todos = get_object_or_404(Todo,id=task_id)
    if request.method == "POST":
        todos.todo_title  = request.POST.get('todo_title')
        todos.todo_description = request.POST.get('todo_description')
        todos.save()
        return redirect('view_tasks')
    return render(request,'edit_task.html',{'todos':todos})


@login_required  
def delete_task(request,task_id):
    todos = get_object_or_404(Todo,id=task_id)
    todos.delete()
    return redirect('view_tasks')





#login and register views 



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)


        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('add_task')

    return render(request,"login.html")


def logout_page(request):
    logout(request)
    messages.success(request,'You have sucessfully logged out!')
    return redirect('login_page')
    


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        


        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('/register/')

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
                )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully ")
        return redirect('login_page')

    return render(request,'register.html')

       






