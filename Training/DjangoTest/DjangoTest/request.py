#encoding=utf-8
from django.http import HttpResponse

# HttpRequest对象包含当前请求URL的一些信息：
#
# 属性/方法 	说明 	举例
# request.path 	除域名以外的请求路径，以正斜杠开头 	"/hello/"
# request.get_host() 	主机名（比如，通常所说的域名） 	"127.0.0.1:8000" or "www.example.com"
# request.get_full_path() 	请求路径，可能包含查询字符串 	"/hello/?print=true"
# request.is_secure() 	如果通过HTTPS访问，则此方法返回True， 否则返回False 	True 或者 False

#     request.META
#     是一个Python字典，包含了所有本次HTTP请求的Header信息，比如用户IP地址和用户Agent（通常是浏览器的名称和版本号）。
# 注意，Header信息的完整列表取决于用户所发送的Header信息和服务器端设置的Header信息。
#  这个字典中几个常见的键值有：

#     HTTP_REFERER，进站前链接网页，如果有的话。 （请注意，它是REFERRER的笔误。）

#     HTTP_USER_AGENT，用户浏览器的user - agent字符串，如果有的话。
# 例如： "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17".

#     REMOTE_ADDR
#     客户端IP，如："12.345.67.89" 。(如果申请是经过代理服务器的话，那么它可能是以逗号分割的多个IP地址，如："12.345.67.89,23.456.78.90" 。)
def get_request_meta(request):
    values=request.Meta.items()
    return HttpResponse(values)

# “request.GET和request.POST是类字典对象”，意思是他们的行为像Python里标准的字典对象，但在技术底层上他们不是标准字典对象。
# 比如说，request.GET和request.POST都有get()、keys()和values()方法，你可以用用 for key in request.GET 获取所有的键。
