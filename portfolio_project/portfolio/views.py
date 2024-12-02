from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


images = [
    {'url': 'portfolio/images/photo1.jpg'},
    {'url': 'portfolio/images/photo2.jpg'},
    {'url': 'portfolio/images/photo3.jpg'},
    {'url': 'portfolio/images/photo4.jpg'},
    {'url': 'portfolio/images/photo5.jpg'},
    {'url': 'portfolio/images/photo6.jpg'},
    {'url': 'portfolio/images/photo7.jpg'},
    {'url': 'portfolio/images/photo8.jpg'},
    {'url': 'portfolio/images/photo9.jpg'},
    {'url': 'portfolio/images/photo10.jpg'},
]


def home(request):
    return render(request, 'portfolio/home.html')

def gallery(request):
    return render(request, 'portfolio/gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'portfolio/contact.html')
