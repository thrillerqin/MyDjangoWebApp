from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from .qbmqtt import client_loop

print('qinbao tests')
client_loop()
print('run tests.py')

# Create your tests here.
# 表单
def test_set_form(request):
    return render(request, 'myapp/test_set_form.html')


# 接收请求数据
def test_set(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
