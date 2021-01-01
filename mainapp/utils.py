from .models import News,Blog
from django.db.models import Q
from itertools import chain

def multiple_search(query):
    filter_lookup = Q(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )
    blog_results = Blog.objects.filter(filter_lookup).distinct()
    news_results = News.objects.filter(filter_lookup).distinct()
    result_list = sorted(chain(blog_results, news_results),key=lambda instance: instance.id,reverse=True)
    count = len(result_list)
    return result_list,count