from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.


def class1(request):
    return render(request, 'class1.html')


def kids1(request):
    return render(request, 'kids.html')
