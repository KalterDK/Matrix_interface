from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from matrix import views
from matrix.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', custom_login, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin-panel$', views.admin_panel, name="Admin Panel"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
