from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True, 
	help_text='Unique value for product page URL, created from name.')
	description = models.TextField()
	is_active = models.BooleanField(default=True)
	

class Meta:
	db_table = 'categories'
	ordering = ['-created_at']
	verbose_name_plural = 'Categories'
def __unicode__(self):
	return self.name
@models.permalink
def get_absolute_url(self):
	return ('catalog_category', (), { 'category_slug': self.slug })