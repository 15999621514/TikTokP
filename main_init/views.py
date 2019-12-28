from django.shortcuts import render, HttpResponsePermanentRedirect, HttpResponse
from django.http import FileResponse, StreamingHttpResponse
from django.http import request
from main_init.main import get_url
#导入模块
import sys
import os
import time




def index(request):
    return render(request, 'index.html')



def api_url(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        if url != '':
            if 'http' in url:
                t = get_url(url)
                f = open(t[0], 'rb').read()
                return HttpResponse(f, content_type='audio/mp3')
            else:
                return render(request, '404.html', {'msg': 'URL地址错误'})
        else:
            return render(request, 'index.html', {'msg': 'URL不能为空!'})

    return render(request, '404.html', {'msg': '请使用GET方式请求!'})

# Create your views here.
