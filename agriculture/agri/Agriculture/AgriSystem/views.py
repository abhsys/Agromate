from django.shortcuts import render
from .models import plot
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def plot_view(request):
    reko=plot.objects.all()
    return render(request,'plot.html',{'reko': reko})
