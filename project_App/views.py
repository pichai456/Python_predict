from django.shortcuts import render
import pandas as pd
from .models import Datastudent
from .model.Knn import *
from django.db import connection
# Create your views here.
context = {'course':[
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
        'Physics Laboratory for Engineers 2',]}

def index(request):
    context
    return render(request, 'index.html', {'context':context})

def predicts(request):
    context 
    if request.method == "POST":  
        temp={}
        temp['GPA']                                 =request.POST.get('GPA')
        temp['Society and Environment']             =request.POST.get('Society and Environment')
        temp['English for Communication 1']         =request.POST.get('English for Communication 1')
        temp['Recreation']                          =request.POST.get('Recreation')
        temp['Engineering Drawing']                 =request.POST.get('Engineering Drawing')
        temp['Engineering Materials']               =request.POST.get('Engineering Materials')
        temp['Calculus for Engineers 1']            =request.POST.get('Calculus for Engineers 1')
        temp['Physics for Engineers 1']             =request.POST.get('Physics for Engineers 1')
        temp['Physics Laboratory for Engineers 1']  =request.POST.get('Physics Laboratory for Engineers 1')
        temp['Engineering Mechanics']               =request.POST.get('Engineering Mechanics')
        temp['Basic Engineering Training']          =request.POST.get('Basic Engineering Training')
        temp['Computer Programming']                =request.POST.get('Computer Programming')
        temp['Calculus for Engineers 2']            =request.POST.get('Calculus for Engineers 2')
        temp['Chemistry for Engineers']             =request.POST.get('Chemistry for Engineers')
        temp['Chemistry Laboratory for Engineers']  =request.POST.get('Chemistry Laboratory for Engineers')
        temp['Physics for Engineers 2']             =request.POST.get('Physics for Engineers 2')
        temp['Physics Laboratory for Engineers 2']  =request.POST.get('Physics Laboratory for Engineers 2')
    else:
        print('method POST not woking ')
    inputData = []
    for v in temp:
        inputData.append(temp[v])
    df,departmentListRequirement = cleanData()
    modelOdject = branch(df,departmentListRequirement)
    df_predi = pre_model(modelOdject,inputData)
    labelvalue = select_branch(df_predi)
    # labelvalue.columns = [''] * len(labelvalue.columns)
    print(labelvalue)
    return render(request, 'index.html',{'labelvalue':labelvalue,'context':context})
