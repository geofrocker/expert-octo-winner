from __future__ import unicode_literals
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from markdown_deux import markdown
from .utils import get_read_time
from django_countries.fields import CountryField

# Create your models here.
class Post(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	product_Name=models.CharField(max_length=50)
	slug=models.SlugField(unique=True)
	category=models.CharField(max_length=50)
	description=models.CharField(max_length=50)
	price=models.CharField(max_length=50)
	country = CountryField(blank_label='(select country)')
	location=models.CharField(max_length=200)
	phone=models.CharField(max_length=15)
	image=models.ImageField(upload_to='products/',null=True, blank=True,
		width_field="width_field",
		height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.product_Name

	def __str__(self):
		return self.product_Name

	def get_absolute_url(self):
		return reverse("products:detail", kwargs={"slug": self.slug })
		#return "/posts/%s/" %(self.id)
	class Meta:
		ordering=["-timestamp","-updated"]
	def get_markdown(self):
		content=self.description
		markdown_text=markdown(content)
		return mark_safe(markdown_text)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_Name)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

	# if instance.content:
	# 	html_string=instance.get_markdown()
	# 	read_time_var=get_read_time(html_string)
	# 	instance.read_time=read_time_var
	

pre_save.connect(pre_save_post_receiver,sender=Post)
