from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, "blog/post_list.html", {})

def post_author(request):
    return render(request, "blog/post_author.html", {})
