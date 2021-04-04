# Create your views here.
from django.shortcuts import render
from .forms import InputForms


# Create your views here.


def signup1(request):
    context = {}
    context['form'] = InputForms()
    return render(request, 'sign1.html', context)
