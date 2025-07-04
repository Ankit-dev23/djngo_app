from django.shortcuts import render,HttpResponse

# Create your views here.
def welcome_call(request):
    return HttpResponse(
        f"Hello Test APIs user v1"
    )

def hello(request):
    return HttpResponse(
        f"Hello Test APIs user v2"
    )