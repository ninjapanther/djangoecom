"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render_to_response
#from django.conf.urls.defaults import *
from django.conf.urls.static import static
from ecom import settings
from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view
from .views import home_page, about_page, contact_page, login_page, register_page
urlpatterns = [
	url(r'^$', 'ecom.views.home'),
	url(r'^$',home_page),
	url(r'^about/$',about_page),
	url(r'^contact/$',contact_page),
	url(r'^login/$',login_page),
	url(r'^register/$',register_page),
	url(r'^products/$',ProductListView.as_view()),
	url(r'^products-fbv/$',product_list_view),
	url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
	url(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^path/to/blog/', include('wordpress.urls')),
	url(r'^catalog/$', 'ecom.views.home'),
	url(r'^myapp/', include('myapp.urls')),
	url(r'^hello/', 'myapp.views.hello', name = 'hello'),
	#url(r'^$', 'products', { 'template_name':'products/index.html'}, 'products_home')
]
