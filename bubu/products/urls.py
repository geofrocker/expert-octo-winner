from django.conf.urls import  url
from bubu.products import views

app_name= 'posts'

urlpatterns = [
	# /shop/
	#ADD PRODUCT URLS
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/picture/$', views.picture, name='picture'),
    url(r'^settings/upload_picture/$', views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', views.save_uploaded_picture,
        name='save_uploaded_picture'),
	url(r'^$', views.post_list, name='products'),
	url(r'^mine/$',views.post_mine, name='list_mine'),
    url(r'^create/$',views.post_create, name='add'),
    url(r'^(?P<slug>[\w-]+)/$',views.post_detail, name='detail'), 
    url(r'^(?P<slug>[\w-]+)/edit/$',views.post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$',views.post_delete),
    
]


