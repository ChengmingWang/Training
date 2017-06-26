#coding=utf-8
from django.http import HttpResponse,Http404
import datetime
"每个视图函数至少要有一个参数，通常被叫作request。 这是一个触发这个视图、包含当前Web请求信息的对象，是类django.http.HttpRequest的一个实例。\
在这个示例中，我们虽然不用request做任何事情，然而它仍必须是这个视图的第一个参数"
def hello(request):
    return HttpResponse("Hello world")

def get_current_time(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):#捕获值永远都是字符串（string）类型，而不会是整数（integer）类型，即使这个字符串全由数字构成
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
        "如果异常没被捕获，将报TypeError异常"
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

