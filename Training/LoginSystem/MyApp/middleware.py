import logging
import datetime

logger = logging.getLogger("myproject.custom")

class GetUserInfoMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = ''
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        logger.info("ip:"+ip+",url:"+request.get_host()+request.get_full_path()+",user:"+request.COOKIES.get('username','no user')+",datetime:"+
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        response = self.get_response(request)
        return response