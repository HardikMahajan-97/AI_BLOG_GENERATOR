from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
# def signup(request):
#     return render(request, 'signup.html')
# def login(request):
#     return render(request, 'login.html')
# def blog_details(request):
#     return render(request, 'blog-details.html')
# def all_blogs(request):
#     return render(request, 'all-blogs.html')
