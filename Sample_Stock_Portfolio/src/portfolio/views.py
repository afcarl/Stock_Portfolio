from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings

import json
import requests


# Create your views here.

def my_view(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))


def invoke_rest(endpoint, body=None, params=None):
    url = '%s%s' % (settings.BENZINGA_API_URL, endpoint)
    try:
        if body:
            resp = requests.post(url.encode('utf-8'), data=body, params=params, timeout=240.0)        
        else:
            resp = requests.get(url.encode('utf-8'), params=params, timeout=240.0)
    except requests.RequestException as e:
        js = 'Local Connection Error - %s' % (e.message)
    else:
        try:
            js = json.loads(resp.text)
        except ValueError:
            js = {'non_json_response_body': resp.text}
    return js

def parse_page():
    url = "F"
    data = invoke_rest(url)
    return data

def get_on_page(request):
    disp = parse_page()
    return render(request, 'portfolio.html', disp)