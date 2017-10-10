from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^result.html$', views.result, name='result'),
    url(r'^search/$', views.SearchFormView.as_view(), name='search'),
]