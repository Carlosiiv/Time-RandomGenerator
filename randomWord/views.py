from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.


def random(request):
    # request.session['counter']= 0
    if 'counter' in request.session:
        request.session['counter'] += 1
    #     
    else:
        request.session['counter'] = 0
        
    context = {
        "randomword": get_random_string(length=20),
    }
    return render(request, "randomword.html", context)

def reset(request):
    del request.session['counter']
    return redirect('/random')