from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^articles/(?P<pk>\d+)/comment/$', views.add_comment_to_article, name='add_comment_to_article'),
]