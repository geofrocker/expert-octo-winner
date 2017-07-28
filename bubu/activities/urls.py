from django.conf.urls import url

from bubu.activities import views

urlpatterns = [
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^unfollow/$', views.unfollow, name='unfollow'),
    url(r'^update_followers_count/$', views.update_followers_count, name='update_followers_count'),
]
