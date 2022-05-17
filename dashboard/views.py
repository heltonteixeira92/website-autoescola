from django.shortcuts import render # noqa


# Create your views here.
def dashboard(request):
    context = {}
    return render(request, 'dashboard/index.html', context)
