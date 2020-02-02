from django.urls import path, include
import app1.views

urlpatterns = [

    path('hello_world', app1.views.hello_world),
    path('content', app1.views.article_content),
    path('index', app1.views.get_index_page),
    path('detail/<int:article_id>', app1.views.get_detail_page)
]
