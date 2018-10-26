from django.shortcuts import render

# Create your views here.
def index(request):

    context={
        'tilte':'Latest post',

    }

    return render(request,"posts/index.html", context)
