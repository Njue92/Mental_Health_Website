from django.shortcuts import render


# Create your views here.

def home(request):
    context = {}
    return render(request, 'mental/index.html', context)


def test(request):
    context = {}
    return render(request, 'mental/test.html', context)