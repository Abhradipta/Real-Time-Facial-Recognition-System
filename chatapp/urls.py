from django.contrib import admin 
from django.urls import path,include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.base,name='home'),
    path('accounts/',include('accounts.urls')),
    path('reg/',include('records.urls')),
    path('feed_detect/',include('feeds.urls')),
]
