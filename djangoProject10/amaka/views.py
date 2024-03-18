from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post
from .forms import PostForm
from django.contrib import messages


from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

@login_required
def delete_post(request,id):
    queryset = Post.objects.filter(author =request.user)
    post = get_object_or_404(Post, pk=id)
    context = {'post':post}

    if request.method == 'GET':
        return render (request,'amaka/post_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,'Post deleted')
        return redirect('posts')
@login_required
def edit_post(request,id):

    queryset = Post.objects.filter(author = request.user)
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post),'id':id}
        return render(request,'amaka/post_form.html',context)

    elif request.method == 'POST':

        form = PostForm(request.POST,instance=post)

        if form.is_valid():
            form.save()
            messages.success(request,'The post has been updataed')
            return redirect('posts')
        else:
            messages.error(request,'Please correct the errors:')
            return render(request,'amaka/post_form.html',{'form':form})


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request,'amaka/post_form.html',context)

    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()

            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'amaka/post_form.html',{'form':form})



def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'amaka/home.html', context)


def about(request):
    return render(request, 'amaka/about.html')
