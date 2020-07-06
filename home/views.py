from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post
from home.models import SearchHistory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime

# Create your views here.

def home(request):
   return render(request, 'Home/home.html')

def about(request):
   return render(request, 'Home/about.html')


def handleSignup(request):
   if request.method == 'POST':
      username = request.POST['username']
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      Password1 = request.POST['Password1']
      Password2= request.POST['Password2']

      #error check
      if len(username) > 10:
         messages.error(request,"Username must be under ten characters")
         return redirect('/')
      if not username.isalnum():
         messages.error(request,"Username should only contains character and numbers")
         return redirect('/')
      if Password1 != Password2:
         messages.error(request,"Password does not match")
         return redirect('/')

      #create user
      myuser = User.objects.create_user(username, email, Password1)
      myuser.first_name = fname
      myuser.last_name = lname
      myuser.save()
      messages.success(request,"Your account has been successfully created")
      return redirect('/')

   else:
      return HttpResponse('404 error')

def handleLogin(request):
   if request.method == 'POST':
      loginusername = request.POST['loginusername']
      loginpassword = request.POST['loginpassword']

      user = authenticate(username=loginusername, password=loginpassword)

      if user is not None:
         login(request,user)
         messages.success(request,'you are logged in')
         return redirect('/')
      else:
         messages.error(request,'invalid username or password, please log in')
         return redirect('/')
def handleLogout(request):
   logout(request)
   messages.success(request,'you are logged out')
   return redirect('/')

def search(request):
   query = request.GET['query']
   if len(query)>78:
      allPosts = Post.objects.none()
   else:
      allPoststitle = Post.objects.filter(title__icontains=query)
      allPostsauthor = Post.objects.filter(author__icontains=query)
      allPostscontent = Post.objects.filter(content__icontains=query)
      allPosts = allPoststitle.union(allPostsauthor,allPostscontent)
      keyword = query
      loginuser = request.user
      now=datetime.datetime.now()
      searchdate = now.strftime("%Y-%m-%d")
      b = SearchHistory(keyword=query, loginuser=loginuser, searchdate=searchdate)
      b.save()
   if allPosts.count() == 0:
      messages.error(request, "No search result found, please search again")
   params = {'allPosts':allPosts, 'query':query}
   return render(request, 'Home/search.html', params)

