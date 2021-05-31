from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import  Post_Kids
def post_kids_list(request):
    object_list = Post_Kids.objects.filter(status='published')
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
      post = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
      post = paginator.page(2)
    except EmptyPage:
     # If page is out of range deliver last page of results
      post = paginator.page(paginator.num_pages)
    return render(request,
    'ListKids/post/lists.html',
    {'page': page,
    'posts': post})
def post_kids_detail(request, year, month, day, post):
    post = get_object_or_404( Post_Kids,
     slug=post,
     status='published',
     publish__year=year,
     publish__month=month,
     publish__day=day)
    post.visits=post.visits+1
    post.save()
    return render(request,
     'ListKids/post/details.html',
     {'posts': post})