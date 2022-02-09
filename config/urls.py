from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.urls import re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('feets/', include('feets.urls', namespace='feets')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('workshops/', include('workshops.urls', namespace='workshops')),
    path('knees/', include('knees.urls', namespace='knees')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}), # 이부분 추가!!
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    