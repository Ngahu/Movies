from django.shortcuts import render


def index(request):
    """returning the home page """
    return render(request, template_name='Movies/index.html')
