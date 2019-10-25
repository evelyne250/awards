from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)