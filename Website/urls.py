
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
]
