from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import movies,gener
# Create your views here.
def index(request):
    # return HttpResponse('what the fuck')
    movie = movies.objects.all()
    return render(request,'index.html',{'movies':movie})

def details(request,movies_id):

    movie=get_object_or_404(movies,pk=movies_id)
    return render(request,'details.html',{ 'movies':movie})