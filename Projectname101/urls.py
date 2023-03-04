from django.contrib import admin
from django.urls import path, include

admin.site.site_header  =  "Club Atlético de Madrid Fans"  
admin.site.site_title  =  "Club Atlético de Madrid Fans | Admin"
admin.site.index_title  =  "Welcome to our online fan page!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
