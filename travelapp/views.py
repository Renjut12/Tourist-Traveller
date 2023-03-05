from django.http import HttpResponse
from django.shortcuts import render
from . models import mytable

# Create your views here.


def indexcycle(request):
       content = mytable.objects.all()
       return render(request,'indexcycle.html',{'key': content})

def aboutcycle(request):
       return render(request,'aboutcycle.html')

def contactcycle(request):
       return render(request,'contactcycle.html')


def cycle(request):
       return render(request,'cycle.html')


def newscycle(request):
       return render(request,'indexcycle.html')










# def About(request):
#     return render(request,'Tourismabout.html')
#
# def Contact(request):
#     return HttpResponse("Department of Tourism, Government of Kerala,Park View, Thiruvananthapuram,Kerala, India - 695 033Phone: +91 471 2321132, Fax: +91 471 2322279,Toll free No: 1-800-425-4747 (within India only)E-mail: info@keralatourism.org")
#
# def Details(request):
#     return render(request,'Tourismdetails.html')
#
# def Thanks(request):
#     return HttpResponse("Thank you")