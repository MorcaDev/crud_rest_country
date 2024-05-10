from django.urls import path
from .views import *

urlpatterns = [
    path('',get_all_country, name="get_all_country"),
    path('<int:pk>/',get_detail_country, name="get_detail_country"),
    path('post/',post_country, name="post_country"),
    path('put/',put_country, name="put_country"),
    path('patch/<int:pk>/',patch_country, name="patch_country"),
    path('delete/',delete_country, name="delete_country"),
    path('delete/<int:pk>/',delete_detail_country, name="delete_detail_country"),
]