from django.http import HttpResponse
from django.shortcuts import render
from .models import place


# Create your views here.
def demo(request):
    obj = place.objects.all()
    return render(request, "Index.html", {'result': obj})

# def about(request):
#     return render(request,"About.html")
#
# def contact(request):
#     return  render(request,"Contact.html")
#
# def gallery(request):
#     return render(request, "Gallery.html")
#
# def pooja(request):
#     return render(request, "Pooja.html")
