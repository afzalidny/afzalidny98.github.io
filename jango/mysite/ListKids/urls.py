from django.urls import path
from .views import post_kids_list,post_kids_detail
app_name = 'ListKids'
urlpatterns = [
 # post views
 path('', post_kids_list, name='post_kids_list'),
 path('<int:year>/<int:month>/<int:day>/<slug:post>/',
 post_kids_detail,
 name='post_kids_detail'),
]