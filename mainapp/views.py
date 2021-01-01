from django.shortcuts import render
from .utils import multiple_search
# Create your views here.


def index(request):
    context = {}
    query = request.GET.get('query')
    if query is not None:
        result_list,count = multiple_search(query)
        context['result_list'] = result_list
        context['count'] = count
        context['query'] = query
    return render(request,'home/index.html',context)