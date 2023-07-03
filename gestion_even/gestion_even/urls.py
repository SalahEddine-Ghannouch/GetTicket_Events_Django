from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import dashboard, login_page, logut_page,dashboard_organ
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('join/', include('usersaccounts.urls')),
    path('Checkout/', include('CheckOut.urls')),
    
    path('admin_events/', dashboard, name='dashboard'),
    path('organ_events/', dashboard_organ, name='dashboard_organ'),
    path('login/', login_page, name='login_admin'),
    path('logout/', logut_page, name='logout_admin'),
    path('events/', include('events.urls')),
    path('organ/', include('organ.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)