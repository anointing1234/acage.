from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve
from django.views.generic import TemplateView
 


urlpatterns = [ 
    path('',views.home,name="home"),        
    path('home/',views.home,name="home"),  
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
# Add media serving for development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
