from django.urls import path
from apps.blogs.views import *

app_name = 'apps/blogs'

urlpatterns = [
# post views
path('', post_list, name='post_list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
]