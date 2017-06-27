import datetime
from django.template import Template, Context
from django.http import HttpResponse

def current_datetime(request):
    now = datetime.datetime.now()
    fp = open('/home/djangouser/templates/tag.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

