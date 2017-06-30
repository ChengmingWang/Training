#user-defined middleware
def simple_middleware(get_response):
    def middleware(request):
        return get_response(request)
    return middleware()
# Or it can be written as a class whose instances are callable, like this:
class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request
        # before the view (and later middleware) are called.
        print 'a'

        response = self.get_response(request)

        # Code to be executed for each request/response
        # after the view is called.
        print 'b'
        return response
