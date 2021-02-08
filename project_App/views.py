from django.shortcuts import render
import pandas as pd
from .models import *
from .model.model_predict import *
from .model.data_requirement import *
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
        input_gpa=[]  
        temp={}
        input_gpa.append(request.POST.get('GPA'))
        temp['society_and_environment']             =request.POST.get('Society and Environment')
        temp['english_for_communication_1']         =request.POST.get('English for Communication 1')
        temp['recreation']                          =request.POST.get('Recreation')
        temp['engineering_drawing']                 =request.POST.get('Engineering Drawing')
        temp['engineering_materials']               =request.POST.get('Engineering Materials')
        temp['calculus_for_engineers_1']            =request.POST.get('Calculus for Engineers 1')
        temp['physics_for_engineers_1']             =request.POST.get('Physics for Engineers 1')
        temp['physics_laboratory_for_engineers_1']  =request.POST.get('Physics Laboratory for Engineers 1')
        temp['engineering_mechanics']               =request.POST.get('Engineering Mechanics')
        temp['basic_engineering_training']          =request.POST.get('Basic Engineering Training')
        temp['computer_programming']                =request.POST.get('Computer Programming')
        temp['calculus_for_engineers_2']            =request.POST.get('Calculus for Engineers 2')
        temp['chemistry_for_engineers']             =request.POST.get('Chemistry for Engineers')
        temp['chemistry_laboratory_for_engineers']  =request.POST.get('Chemistry Laboratory for Engineers')
        temp['physics_for_engineers_2']             =request.POST.get('Physics for Engineers 2')
        temp['physics_laboratory_for_engineers_2']  =request.POST.get('Physics Laboratory for Engineers 2')
    else:
        print('method POST not woking ')
    input_gpa = float(input_gpa[0]) #input GPA
    input_studant = change_input(temp) #input course

    input_predict, df, majors_requirement = data_set_df(input_studant, input_gpa)
    modelOdject = major_model(df, majors_requirement)
    # print(modelOdject)
    df_predi = pre_model(modelOdject,input_predict)
    labelvalue = select_branch(df_predi)
    labelvalue= labelvalue.to_dict('records')[0] 
    print(labelvalue)
    return render(request, 'index.html',{'labelvalue':labelvalue, 'context':context})

