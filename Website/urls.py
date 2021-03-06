
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^cadastrar/funcionario', views.cadastro_funcionario, name='cadastrar_funcionario'),
    url(r'^cadastrar/assistido', views.cadastro_assistido, name='cadastrar_assistido'),
    url(r'^base', views.template_base, name='template_base'),
    url(r'^agendamento', views.agendamento, name='agendamento'),
    url(r'^dados/usuario', views.dados_usuario, name='dados_usuario'),
    url(r'^table', views.table, name='table'),
]
