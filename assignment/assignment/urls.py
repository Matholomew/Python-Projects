from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from polls import views as myapp_views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]


handler404 = myapp_views.error_404
handler500 = myapp_views.error_500