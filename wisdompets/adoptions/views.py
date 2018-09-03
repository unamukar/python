from django.shortcuts import render
from django.http import HttpResponse

def home(request):return HttpResponse('<p>Home view</p>')
def pet_detail(request,id):return HttpResponse('<p>Pet_detail vew with the id {}</p>'.format(id))
# Create your views here.
