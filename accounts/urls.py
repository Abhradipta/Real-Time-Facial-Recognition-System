from django.urls import path
from . import views

urlpatterns = [    
    path('signin/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='prof'),
    path('logs/',views.logs,name='logs'),
    path('about/',views.about,name='about'),
]
