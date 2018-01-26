from django.shortcuts import render

# Create your views here.
def catalog(request):
	my_context = Context({ 'site_name': 'Modern Musician' })
	response_html = return_to_string('sample.html', my_context)
	return HttpResponse(response_html)