from django.shortcuts import get_object_or_404


from django.shortcuts import render
from .models import Blog

def all_blogs(request):

#we did the {{blog.count}} in the all_blog.html file, but that will show the clogs that are present 
#that will not taken the remaining hidden (outdated) blogs 
#-------man, i thought of writing a program for this, but i have no idea ---- so remove [:5]
    blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')
    #ordering the blog and getting the last 5 blogs only
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def details(request, blog_id):

#to take 1 particular blog, import get_ibject_or_404
    blog = get_object_or_404(Blog, pk = blog_id)
#grab the number and display the corresponding blog_id
    return render(request, 'blog/details.html', {'blog':blog})



