from django.urls import path
from . import views



app_name = 'blog'

urlpatterns = [
    path('',views.post_list , name='post_list' ),
    path('<int:id>' , views.post_detail , name='post_detail'),
    path('tags=<slug:tag>' , views.post_by_tag , name='post_by_tag'),
    path('category=<slug:category>' , views.post_by_category , name='post_by_category'),
]