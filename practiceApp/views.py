from django.http import HttpResponse
from django.shortcuts import render
from practiceApp.models import sportsPost, sportsCategory

# Create your views here.
def home(request):
    posts = sportsPost.objects.all()[:11]
    categorys = sportsCategory.objects.all()
    # print(posts)
    postData = {
        'sportsPost': posts,
        'categorys': categorys
    }
    return render(request, 'home.html', postData)

def post(request, url):
    post = sportsPost.objects.get(urls=url)
    categorys = sportsCategory.objects.all()
    return render(request, 'post.html', {'post': post, 'categorys': categorys})

def category(request, url):
    category = sportsCategory.objects.get(urls=url)
    posts = sportsPost.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'posts': posts})