from django.shortcuts import render
import pandas as pd
from .models import Datastudent
# Create your views here.

def predict(request):
    context={}
    # if request.method == "POST":
    #     temp={}
    #     temp['Society and Environment']=request.POST.get('Society and Environment')
    #     temp['English for Communication 1']=request.POST.get('English for Communication 1')
    #     temp['Recreation']=request.POST.get('Recreation')
    #     temp['Engineering Drawing']=request.POST.get('Engineering Drawing')
    #     temp['Engineering Materials']=request.POST.get('Engineering Materials')
    #     temp['Calculus for Engineers 1']=request.POST.get('Calculus for Engineers 1')
    #     temp['Physics for Engineers 1']=request.POST.get('Physics for Engineers 1')
    #     temp['Physics Laboratory for Engineers 1']=request.POST.get('Physics Laboratory for Engineers 1')
    #     temp['Engineering Mechanics']=request.POST.get('Engineering Mechanics')
    #     temp['Basic Engineering Training']=request.POST.get('Basic Engineering Training')
    #     temp['Computer Programming']=request.POST.get('Computer Programming')
    #     temp['Calculus for Engineers 2']=request.POST.get('Calculus for Engineers 2')
    #     temp['Chemistry for Engineers']=request.POST.get('Chemistry for Engineers')
    #     temp['Chemistry']=request.POST.get('Chemistry')
    #     temp['Laboratory for Engineer']=request.POST.get('Laboratory for Engineer')
    #     temp['Physics for Engineers 2']=request.POST.get('Physics for Engineers 2')
    #     temp['Physics Laboratory for Engineers 2']=request.POST.get('Physics Laboratory for Engineers 2')
    #     temp['Year 1,Semester 1']=request.POST.get('Year 1,Semester 1')
    #     testData = pd.DataFrame({'x': temp}).transpose()
    return render(request, 'test.html', context) 

def lists(request):
     context = {'course':[
        'GPA',
        'Society and Environment',
        'English for Communication 1',
        'Recreation',
        'Engineering Drawing',
        'Engineering Materials',
        'Calculus for Engineers 1',
        'Physics for Engineers 1',
        'Physics Laboratory for Engineers 1',
        'Engineering Mechanics',
        'Basic Engineering Training',
        'Computer Programming',
        'Calculus for Engineers 2',
        'Chemistry for Engineers',
        'Chemistry Laboratory for Engineers',
        'Physics for Engineers 2',
        'Physics Laboratory for Engineers 2',
          ]}
     return render(request, 'index.html', context)

def display(request):
    data = Datastudent.objects.all()   
    context = {
        'a':data
    }
    Data = pd.DataFrame({'x': data}).transpose()

    return render(request, 'display.html', context)