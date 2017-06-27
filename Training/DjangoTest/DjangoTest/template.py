#encoding=utf-8
import datetime
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
def current_datetime(request):
    now = datetime.datetime.now()
<<<<<<< HEAD
    # t=Template("<p>{{date}}<p>")
    t = get_template("current_datetime.html")
=======
    fp = open('/home/djangouser/templates/tag.html')
    t = Template(fp.read())
    fp.close()
>>>>>>> adfaddf580b3b2a83be14e6bf28355782b2fcb8e
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

from django.shortcuts import render_to_response
def current_datetime2(request):
    return render_to_response('current_datetime.html',Context({'current_date': datetime.datetime.now()}))

def current_datetime3(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
#  locals() 的值，它囊括了函数执行到该时间点时所定义的一切变量。
# 因此，我们将 now 变量重命名为 current_date ，因为那才是模板所预期的变量名称。
# 在本例中， locals() 并没有带来多 大 的改进，但是如果有多个模板变量要界定而你又想偷懒，这种技术可以减少一些键盘输入。
# 使用 locals() 时要注意是它将包括 所有 的局部变量，它们可能比你想让模板访问的要多。
# 在前例中， locals() 还包含了 request 。对此如何取舍取决你的应用程序。

