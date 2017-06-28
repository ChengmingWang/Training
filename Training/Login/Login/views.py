from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import auth

def set_cookie(request):
    if "favorite_color" in request.GET:
        color=request.GET["favorite_color"]
        response= HttpResponse("Your favorite color is %s" % color)
        response.set_cookie("favorite_color",color)
        return response
    else:
        return HttpResponse("You don't have a favorite color.")

def get_cookie(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % request.COOKIES["favorite_color"])
    else:
        return HttpResponse("You don't have a favorite color.")

def validate_user(request):
    return HttpResponse("")