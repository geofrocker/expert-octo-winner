try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post
from PIL import Image

from django_countries.widgets import CountrySelectWidget


# Create your views here.

def post_create(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user=request.user
		instance.save()
		messages.success(request, "Successfully Created", extra_tags="success")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context={
		"form":form,
	}
	return render(request,"products/post_form.html",context)

def post_detail(request, slug=None):#retrieve
	
	instance = get_object_or_404(Post, slug=slug)
	share_string = quote_plus(instance.description)

	
	context = {
		"title": instance.product_Name,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "products/post_detail.html", context)
	return render(request, "products/post_list.html", context)
@login_required
def post_list(request):#list items
	today=timezone.now().date()
	queryset_list=Post.objects.order_by("-timestamp")
	
	context={
		"object_list":queryset_list,
		"today":today,
		}
	return render(request,"products/post_list.html",context)

def post_mine(request):#list items
	today=timezone.now().date()
	queryset_list=Post.objects.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		#user_id=1
		queryset_list=Post.objects.filter(user_id=request.user).order_by("-timestamp")
	search=request.GET.get("q")
	if search:
		queryset_list=queryset_list.filter(
			Q(product_Name__icontains=search)|
			Q(description__icontains=search)|
			Q(user__first_name__icontains=search)|
			Q(user__last_name__icontains=search)
			).distinct()
	paginator=Paginator(queryset_list,16)
	page=request.GET.get('page')
	try:
		queryset=paginator.page(page)
	except PageNotAnInteger:
		queryset=paginator.page(1)
	except EmptyPage:
		queryset=paginator.page(paginator.num_pages)

	context={
		"object_list":queryset,
		"product_Name":"List",
		"today":today,
		}
	return render(request,"products/post_list.html",context)


def post_update(request,  slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance=get_object_or_404(Post,slug=slug)
	form=PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, "Post Edited Successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context={
		"product_Name":instance.product_Name, 
		"instance":instance,
		"form":form,
		}
	return render(request,"products/post_form.html",context)

def post_delete(request,  slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance=get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Post Deleted Successfully")
	return redirect("posts:list")

@login_required
def settings(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user=request.user
		instance.save()
		messages.add_message(request,
		messages.SUCCESS,
		'Your profile was successfully edited.')
	context={
	"form":form,
	}
	return render(request, 'products/settings.html',context)


@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True

    except Exception:
        pass

    return render(request, 'products/picture.html',
                  {'uploaded_picture': uploaded_picture})


@login_required
def upload_picture(request):
    try:
        product_images = django_settings.MEDIA_ROOT + '/product_images/'
        if not os.path.exists(product_images):
            os.makedirs(product_images)
        f = request.FILES['picture']
        filename = product_images + Product.id + '_tmp.jpg'
        with open(filename, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        im = Image.open(filename)
        width, height = im.size
        if width > 350:
            new_width = 350
            new_height = (height * 350) / width
            new_size = new_width, new_height
            im.thumbnail(new_size, Image.ANTIALIAS)
            im.save(filename)


        return redirect('/settings/picture/?upload_picture=uploaded')

    except Exception as e:
        print(e)
        return redirect('/settings/picture/')


@login_required
def save_uploaded_picture(request):
    try:
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        w = int(request.POST.get('w'))
        h = int(request.POST.get('h'))
        tmp_filename = django_settings.MEDIA_ROOT + '/product_images/' +\
            Product.id + '_tmp.jpg'
        filename = django_settings.MEDIA_ROOT + '/product_images/' +\
            Product.id + '.jpg'
        im = Image.open(tmp_filename)
        cropped_im = im.crop((x, y, w+x, h+y))
        cropped_im.thumbnail((200, 200), Image.ANTIALIAS)
        cropped_im.save(filename)
        os.remove(tmp_filename)

    except Exception:
        pass

    return redirect('/settings/picture/')	 