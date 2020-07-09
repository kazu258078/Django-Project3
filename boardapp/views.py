from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    # users = User.objects.all()
    # user1 = User.objects.get(username='kazu')
    # print("Users", users)
    # print("user1", user1)
    # print("user1 Email", user1.email)
    # print("Method:", request.method)
    if request.method == "POST":
        #print("Request Post", request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error':'This user is already registered'})
        except:
            User.objects.create_user(username, '', password)
            return redirect('login')
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirectは名前からURLを呼び出して、そのURLを改めてrequestしそのページに遷移していく
            # 呼び出された"login/"に対して"signup/"というrequestを改めて呼ぶ
            return redirect('list')
            
            # renderは受け取ったrequestに対してHTMLとデータを入れ込んでresponseを返すのでURLは変わらない
            # 呼び出された"login/"に対してのresponseとしてsignup.htmlを返している
            #return render(request, 'signup.html')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = BoardModel.objects.get(id=pk)
    return render(request, 'detail.html', {'object':object})

@login_required
def goodfunc(request, pk):
    post = BoardModel.objects.get(id=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

@login_required
def readfunc(request, pk):
    post = BoardModel.objects.get(id=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')