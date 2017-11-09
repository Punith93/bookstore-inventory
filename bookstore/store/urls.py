from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^create$',views.create, name='create'),
    url(r'^Createbook$',views.Createbook, name='Createbook'),
    url(r'^Delete/(?P<id>\d+)$',views.Delete, name='Delete'),
    url(r'^Edit/(?P<id>\d+)$',views.Edit, name='Edit'),
    url(r'^update/(?P<id>\d+)$',views.update, name='update'),
]