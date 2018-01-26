from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.
#def hello(request):
   #text = """<h1>welcome to my app !</h1>"""
   #return render(request, "myapp/hello.html", {})
def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "myapp/hello.html", {"today" : today})
def morning(request):
   text = """<h1>welcome to my app !</h1>"""
   return render(request, "myapp/morning.html", {})
 
def article(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)
   
def articles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)