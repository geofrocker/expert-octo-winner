from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from bubu.activities import views as activities_views
from bubu.authentication import views as bubu_auth_views
from bubu.core import views as core_views
from bubu.products import views as product_views
from bubu.search import views as search_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', bubu_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^feeds/', include('bubu.feeds.urls')),
    url(r'^questions/', include('bubu.questions.urls')),
    url(r'^activity/', include('bubu.activities.urls')),
    url(r'^products/', include('bubu.products.urls', namespace='products')),
    url(r'^articles/', include('bubu.articles.urls')),
    url(r'^messages/', include('bubu.messenger.urls')),
    url(r'^notifications/$', activities_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications,
        name='check_notifications'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    url(r'^(?P<username>[^/]+)/following/$', activities_views.following, name='following'),
    url(r'^(?P<username>[^/]+)/followers/$', activities_views.followers, name='followers'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
