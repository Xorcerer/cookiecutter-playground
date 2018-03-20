from django.conf.urls import include, url
from echo import views


urlpatterns = [
    url(r'^echo$', views.echo),
]
    