from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<idr>\d+)$', views.books),
    url(r'^process$', views.process),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<idr>\d+)$', views.show_author),
    url(r'^process/authors$', views.process_author),
]


