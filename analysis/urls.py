from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^your-query/', views.get_query),
    url(r'^your-selection/', views.get_selection),
    # url(r'^bar/$', view=views.BarView.as_view(), name='bar')
    # url(r'^bar/', views.BarView.as_view()),
]