from django.shortcuts import render,redirect
from blog0.models import postModel,categoryModel,commentModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

@permission_required('blog0.view_postmodel', login_url='/post/login')
def postList(request):
    posts = postModel.objects.all()
    return render(request, 'postList.html', {"posts":posts})

@permission_required('blog0.add_postmodel', login_url='/post/login')
def postCreate(request):
    if request.method == "GET":
        category = categoryModel.objects.all()
        return render(request, 'postCreate.html',{'category':category})
    if request.method == "POST":
        posts = postModel.objects.create(
            title = request.POST.get("title"),
            content = request.POST.get("body"),
            image = request.FILES.get("image"),
            category_id = request.POST.get('category'),
            author_id = request.user.id,
            created_at = request.POST.get("date")
        )
        posts.save()
        messages.success(request, "The post has been created successfully")
        return redirect('/post/list')

@permission_required('blog0.view_postmodel', login_url='/post/login')
def postDetail(request,post_id):
    posts = postModel.objects.get(id=post_id)
    return render(request, 'postDetail.html',{'posts':posts})

@permission_required('blog0.change_postmodel', login_url='/post/login')
def postUpdate(request,post_id):
    if request.method == "GET":
        posts = postModel.objects.get(id=post_id)
        category = categoryModel.objects.all()
        return render(request, 'postUpdate.html', {'posts':posts,'category':category})
    if request.method == "POST":
        posts = postModel.objects.get(id=post_id)
        posts.title = request.POST.get('title')
        posts.content = request.POST.get('body')
        posts.category_id = request.POST.get('category')
        if request.FILES.get('image'):
            posts.image = request.FILES.get('image')    
        posts.save()
        messages.success(request, "The post has been updated successfully")
        return redirect('/post/list/')

@permission_required('blog0.delete_postmodel', login_url='/post/login')
def postDelete(request,post_id):
    posts = postModel.objects.get(id=post_id)
    posts.delete()
    messages.success(request, "The post has been deleted")
    return redirect('/post/list/')

def login_view(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('/post/list/')
        else:
            messages.error(request,"Incorrect!")
            return redirect('/post/login/')

def logout_view(request):
    logout(request)
    return redirect('/post/login/')
