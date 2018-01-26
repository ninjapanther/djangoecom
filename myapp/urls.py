from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('myapp.views', url(r'^hello/', 'hello', name = 'hello'),
   url(r'^morning/', 'morning', name = 'morning'),
      url(r'^article/(\d+)/', 'article', name = 'article'),
	     url(r'^admin/', include(admin.site.urls)),
		    url(r'^articles/(\d{2})/(\d{4})', 'articles', name = 'articles'),
)
