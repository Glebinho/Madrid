from django.contrib import admin
from django.urls import path, include

from base.views import *
admin.site.site_header  =  "Club Real Madrid Fans"
admin.site.site_title  =  "Club Real Madrid Fans | Admin"
admin.site.index_title  =  "Welcome to our online fan page!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
handler404 = pageNotFound