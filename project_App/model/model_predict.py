import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler,Normalizer
from project_App.models import *
from django.db import connection
import json
 
def model_Knn(major, df):
    df = df[df['major_name'] == major]
    df = df.reset_index(drop=True)

    X = df.drop([
        'GPAX',
        'GPAX_char',
        'major_name', 
        ], axis='columns').values
    y = df['GPAX_char'].values
        
    param_grid = dict(n_neighbors=range(1, 10))
    model = KNeighborsClassifier(metric='euclidean')
    model = GridSearchCV(model, param_grid, cv=5)
    # print(model.best_params_)
    model.fit(X, y)
    return  model

def model_Regression(major, df):
    df = df[df["major_name"] == major]
    df = df.reset_index(drop=True)

    X = df.drop([
        'GPAX',
        'GPAX_char',
        'major_name',
    ], axis='columns')

    y = df['GPAX']

    # สร้าง model
    model = LinearRegression()

    #Fitting Model
    model.fit(X,y)

    # วัดประสิทธิภาพ
    y_pred = model.predict(X)

    # ค่าสัมประสิทธิ์การตัดสินใจ
    r_squared = model.score(X, y)

    # intercept
    intercept = model.intercept_

    # slope ความลาดชัน ตามลำดับจำนวน column แกน X 
    slope = model.coef_

    return major, model, r_squared, intercept, slope

def model_Dtree(major, df):
    df = df[df['major_name'] == major]
    df = df.reset_index(drop=True)

    X = df.drop([
        'GPAX',
        'GPAX_char',
        'major_name', 
        ], axis='columns').values
    y = df['GPAX_char'].values

    model = DecisionTreeClassifier(
        criterion="entropy",
        splitter='best',
        max_depth=5,
        min_samples_split=2,
        min_samples_leaf=1,
        min_weight_fraction_leaf=0,
        max_features=None,
        random_state=None,
        max_leaf_nodes=None,
        min_impurity_decrease=0,
        min_impurity_split=None,
        class_weight=None,
    )
    model.fit(X, y)
    return model
    
def model_NN(major, df):
    df = df[df['major_name'] == major]
    df = df.reset_index(drop=True)

    X = df.drop([
        'GPAX',
        'GPAX_char',
        'major_name', 
        ], axis='columns').values
    y = df['GPAX_char'].values
    
    model = MLPClassifier(hidden_layer_sizes=13, max_iter=500)
    model.fit(X, y)
    
    return  model
       
def major_model(df,majors_requirement):
    modelOdject = []
    for major in majors_requirement:
        print(major)
        # model = model_Knn(major, df)
        model = model_Dtree(major, df)
        # model = model_NN(major, df)
        branchNameML, modelMLinear, r_squared, intercept, slope = model_Regression(major, df)
        modelOdject.append({
            'Name':             major,
            'model':           model, 
            'modelMLinear': modelMLinear,
            'r_squared' : r_squared,
            'intercept' : intercept,
            # 'slope' : slope    
        })
    return modelOdject     
     
def pre_model(modelOdject,input_predict):
    # Dataframe แสดง ผลลัพท์
    df_predi = pd.DataFrame(columns=[
        'สาขา',
        'ผลการเรียน 2.00 - 2.75',
        'ผลการเรียน 2.76 - 3.24',
        'ผลการเรียน 3.25 - 4.00'
    ])
    
    # loop นำค่าใน ModelOdject มาใส่ Dataframe
    for i in modelOdject:
        # ทำนาย

        answer = i['model'].predict([input_predict])
        answer_mlinear = i['modelMLinear'].predict([input_predict])[0]
        
        new_row = {
            'สาขา' : i['Name'],
            'ผลการเรียน 2.00 - 2.75' : 0,
            'ผลการเรียน 2.76 - 3.24' : 0,
            'ผลการเรียน 3.25 - 4.00' : 0,
            'GPA_Pre':round(answer_mlinear,2)

        }

        if answer[0] == 'L':
            new_row['ผลการเรียน 2.00 - 2.75'] = 1
        elif answer[0] == 'M':
            new_row['ผลการเรียน 2.76 - 3.24'] = 1
        elif answer[0] == 'H':
            new_row['ผลการเรียน 3.25 - 4.00'] = 1

        df_predi = df_predi.append(new_row, ignore_index=True)
    return df_predi

def select_branch(df_predi):
    count = 3
    labelvalue = pd.DataFrame()
    while count >= 1:
        labelvalue = df_predi.loc[df_predi[df_predi.columns[count]] == 1]
        if len(labelvalue):
            df_Namebranch = labelvalue[labelvalue.columns[0]]
            df_predictGPA = labelvalue['GPA_Pre']
            df_value = labelvalue[labelvalue.columns[count]]

            labelvalue = pd.merge(df_Namebranch, df_value, left_index=True, right_index=True)
            labelvalue = pd.merge(labelvalue, df_predictGPA, left_index=True, right_index=True)

            labelvalue = labelvalue[labelvalue['GPA_Pre'] == labelvalue['GPA_Pre'].max()]
            break
        else :
            count -= 1
        
    return labelvalue