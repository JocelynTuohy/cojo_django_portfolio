from django.conf.urls import url
from . import views
app_name = 'portfolioapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'testimonials', views.testimonials, name='testimonials'),
]