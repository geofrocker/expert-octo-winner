from django.contrib import admin
from .models import Activity,Notification,Followers
# Register your models here.
admin.site.register(Activity)
admin.site.register(Notification)
admin.site.register(Followers)
