from django.shortcuts import render
from .models import Books

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse, Http404
# import HttpResponse and Http404 from django.http


def home_view(request, *args, **kwargs):
   return HttpResponse("<h1>Hello World!</h1>")


# def book_detail_view(request, book_id, *args, **kwargs):
#     # obj = Books.objects.get(id=book_id)
#     # in book_detail_view function 
#     try:
#         obj = Books.objects.get(id=book_id)
#     except:
#         raise Http404
#     return HttpResponse(f"Name: {obj.name} Author: {obj.author}")