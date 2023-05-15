from django.urls import path

from blog import views
#importing the views.py from the portfolio

#inorder to access the blog title with likable link, we add this 
#
app_name = 'blog'
#

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.details, name = 'details'),
#if you get an integer, pass to views.detail with method 'details'
]