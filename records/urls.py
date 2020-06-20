from django.urls import path
from . import views

urlpatterns = [    
    path('add/',views.face,name='reg-face'),
    path('addface/',views.get_face,name='add-face'),
    path('pics/',views.fetch,name='pic'),
    path('addfaceremote/',views.get_face_remote,name='add-face-remote'),
]
