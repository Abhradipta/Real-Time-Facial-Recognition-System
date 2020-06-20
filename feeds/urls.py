from django.urls import path
from . import views

urlpatterns = [    
    path('feeds-detect/',views.detection,name='feed-detect'),
    path('detect-remote/',views.init_url,name='with_url'),
    path('detect-local/',views.init_server,name='without_url'),
    path('handler-start/',views.start,name='start'),
    path('handler-end/',views.end,name='end'),
    path('handler-train/',views.train,name='train'),
]
