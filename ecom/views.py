from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from .forms import ContactForm, LoginForm, RegisterForm
def home(request):
	return render_to_response(u'index.html')
def home_page(request):
	context = {
	"title":"11home",
	"content":"11homepage content all details"
	}
	return render(request,"home_page.html",context)
def catalog(request):
	my_context = Context({ 'site_name': 'Modern Musician' })
	response_html = return_to_string('sample.html', my_context)
	return HttpResponse(response_html)

def about_page(request):
	return render(request,"about_page.html",{})
	
def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"contact",
		"content":"welcome to contact page",
		"form":contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	#if request.method == "POST":
		#print(request.POST)
		#print(request.POST.get('fullname'))
		#print(request.POST.get('email'))
		#print(request.POST.get('content'))
	return render(request,"contact/view.html",context)
def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
		}
	print("USer logged in")
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		#context['form'] = LoginForm()
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username, password=password)
		print(request.user.is_authenticated())
		if user is not None:
			print(request.user.is_authenticated())
			login(request,user)
			return redirect("/login")
		else:
			print("Error")
			#context['form'] = LoginForm()
	return render(request,"auth/login.html",context)
def register_page(request):
	form = LoginForm(request.POST or None)
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)

	return render(request,"auth/register.html",{})
	
def home_page_old(request):
	html_ = """
	<!doctype html>
   <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>
  </body>
  </html>
    """
	return HttpResponse(html_)
	
	
def home_page_old(request):
	return HttpResponse("hello world")