from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def menu(request):
    return render(request, 'main/menu.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def contact(request):
    return render(request, 'main/contact.html')
