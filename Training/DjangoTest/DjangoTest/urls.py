#coding=utf-8
"""DjangoTest URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import hello,get_current_time,hours_ahead,search_form,search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', hello),
    url(r'^time$',get_current_time),
    url(r'^search-form/$', search_form),
url(r'^search/$', search),
    url(r'^time/plus/(\d{1,2})',hours_ahead),# 1-2位的数字,
# 正则表达式字符串的开头字母“r”。 它告诉Python这是个原始字符串，不需要处理里面的反斜杠（转义字符）。
# 在普通Python字符串中，反斜杠用于特殊字符的转义。比如n转义成一个换行符。
# 当你用r把它标示为一个原始字符串后，Python不再视其中的反斜杠为转义字符。也就是说，“n”是两个字符串：“”和“n”。
# 由于反斜杠在Python代码和正则表达式中有冲突，因此建议你在Python定义正则表达式时都使用原始字符串。 从现在开始，本文所有URL模式都用原始字符串。
]

#     首先，我们从模块 (在 Python 的 import 语法中， mysite/views.py 转译为 mysite.views ) 中引入了 hello 视图。 （这假设mysite/views.py在你的Python搜索路径上。
# 关于搜索路径的解释，请参照下文。）
#     接下来，我们为urlpatterns加上一行： (‘^hello/$’, hello), 这行被称作URLpattern，它是一个Python的元组。
# 元组中第一个元素是模式匹配字符串（正则表达式）；第二个元素是那个模式将使用的视图函数。
# 简单来说，我们只是告诉 Django，所有指向 URL /hello/ 的请求都应由 hello 这个视图函数来处理。
# 举例来说，假定你将 Python 路径设置为 ['','/usr/lib/python2.4/site-packages','/home/username/djcode/'] 。如果执行代码 from foo import bar ，
# Python 将会首先在当前目录查找 foo.py 模块( Python 路径第一项的空字符串表示当前目录)。 如果文件不存在，Python将查找 /usr/lib/python2.4/site-packages/foo.py 文件。
# 最好还是用范例来说明一下这个概念。 如果我们用尾部不是$的模式’^hello/’，那么任何以/hello/开头的URL将会匹配，例如：/hello/foo 和/hello/bar，而不仅仅是/hello/。
# 类似地，如果我们忽略了尖号(^)，即’hello/$’，那么任何以hello/结尾的URL将会匹配，例如：/foo/bar/hello/。
# 如果我们简单使用hello/，即没有^开头和$结尾，那么任何包含hello/的URL将会匹配，如：/foo/hello/bar。因此，我们使用这两个符号以确保只有/hello/匹配，不多也不少。
# 你大多数的URL模式会以^开始、以$结束，但是拥有复杂匹配的灵活性会更好。
# 你可能会问：如果有人申请访问/hello（尾部没有斜杠/）会怎样。
# 因为我们的URL模式要求尾部有一个斜杠(/)，那个申请URL将不匹配。
# 然而，默认地，任何不匹配或尾部没有斜杠(/)的申请URL，将被重定向至尾部包含斜杠的相同字眼的URL。 （这是受配置文件setting中APPEND_SLASH项控制的，参见附件D。）