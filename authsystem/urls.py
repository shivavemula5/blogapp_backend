from django.contrib import admin
from django.urls import path , include
from blogposts import views 
from blogposts.api import views as api_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('api/',include('blogposts.urls')),
    path('api/stripe/',include('payments.urls')),
]
