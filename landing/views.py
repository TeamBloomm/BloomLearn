from django.shortcuts import render


# Create your views here.
def landing_page(request):
    return render(request, 'landing/landing_page.html', {})

def select_role(request):
    return render(request, 'landing/select_role.html', {})