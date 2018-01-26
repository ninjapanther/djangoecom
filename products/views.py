from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from .models import Product
class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"
	
	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object': queryset
	}
	return render(request, "products/list.html", context)
class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"
	#def get_context_data(self, *args, **kwargs):
		#context = super(ProductListView, self).get_context_data(*args,**kwargs)
		#print(context)
		#return context
		
#get_context_data(abc, 123, fhgjhhj, another=abc,abc=123)
	
def product_detail_view(request, pk=None, *args, **kwargs):
	#print(args)
	#print(kwargs)
	instance = Product.objects.all(pk=pk)
	instance = get_object_or_404(Product, pk=pk)
	context = {
		'object': instance
	}
	return render(request, "products/detail.html", context)
