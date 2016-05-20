from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.

def my_view(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))