from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = User.objects.create(name=request.user)
			user = User.objects.get(username=request.user.username)
			post.author = user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', post_id=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})	

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            print("User: " + str(request.user))
            #post.author = User.objects.create(name=request.user)
            user = User.objects.get(username=request.user.username)
            post.author = user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})	