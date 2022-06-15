from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "webapp"

urlpatterns = [
    path("", views.uploadFile, name = "uploadFile"),
    path('/home/signup', views.signup, name = 'signup'),
    path('/home/login', views.login, name = 'login'),
    path('/home/logout', views.logout, name = 'logout'),
    path('/home', views.home, name = 'home'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )