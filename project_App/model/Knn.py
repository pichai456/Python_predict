import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler,Normalizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from project_App.models import Datastudent
from django.db import connection

def cleanData():
    query = str(Datastudent.objects.all().query)
    df = pd.read_sql_query(query, connection)
    df.dropna(axis=0, inplace=True)
    labelEn = LabelEncoder()
    # ภาคที่เปิดรับ หลักสาขา
    departmentListRequirement = np.array([
        'ภาควิชาวิศวกรรมสิ่งทอ',
        'ภาควิชาวิศวกรรมอิเล็กทรอนิกส์และโทรคมนาคม',
        'ภาควิชาวิศวกรรมอุตสาหการ',
        'ภาควิชาวิศวกรรมเกษตร',
        'ภาควิชาวิศวกรรมวัสดุและโลหะการ',
        'ภาควิชาวิศวกรรมเคมี',
        'ภาควิชาวิศวกรรมเครื่องกล',
        'ภาควิชาวิศวกรรมโยธา',
        'ภาควิชาวิศวกรรมคอมพิวเตอร์',
        'ภาควิชาวิศวกรรมไฟฟ้า',
    ])
    grade = []
    df = df[df["ภาควิชา"].isin(departmentListRequirement)]
    df = df.reset_index(drop=True)
    for value in df['GPA จบ']:
        if value >= 2.00 and value <= 2.50 :
            grade.append('L')
        elif value >= 2.51 and value <= 3.25 :
            grade.append('M')
        elif value >= 3.26 and value <= 4.00 :
            grade.append('H')
    df['GPA จบlevel'] = grade    
    return df,departmentListRequirement

def branch(df,departmentListRequirement):
    modelOdject = []
    for branch in departmentListRequirement:
        print(branch)
        knn_best = Model_Knn(branch, df)
        branchNameML, modelMLinear, r_squared, intercept, slope = Model_Regression(branch, df)
        modelOdject.append({
            'Name':             branch,
            'model':           knn_best, 
            'modelMLinear': modelMLinear,
            'r_squared' : r_squared,
            'intercept' : intercept,
            'slope' : slope    
        })
    return modelOdject

def Model_Knn(branch, df):
    df = df[df['ภาควิชา'] == branch]
    df = df.reset_index(drop=True)

    X = df.drop([
        'รหัสนักศึกษา',
        'GPA จบ', 
        'id_departments', 
        'ภาควิชา', 
        'id_branch',
        'รหัสสาขา', 
        'สาขาวิชา', 
        'ปีเข้าศึกษา',
        'GPA จบlevel',], axis=1).values
    
    y = df['GPA จบlevel'].values

    # X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.32 , random_state=26)
    
    param_grid = dict(n_neighbors=range(1, 51))
    
    knn = KNeighborsClassifier(metric='euclidean')
    knn_best = GridSearchCV(knn, param_grid, cv=10)
    knn_best.fit(X, y)
    # y_pred = knn_best.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # precision = precision_score(y_test, y_pred, average="macro")
    # recall = recall_score(y_test, y_pred,average="macro")
    
    return  knn_best

def Model_Regression(branch, df):
    df = df[df["ภาควิชา"] == branch]
    df = df.reset_index(drop=True)

    # ข้อมูล Attribute
    X = df.drop([
        'รหัสนักศึกษา',
        'GPA จบ', 
        'id_departments', 
        'ภาควิชา', 
        'id_branch',
        'รหัสสาขา', 
        'สาขาวิชา', 
        'ปีเข้าศึกษา',
        'GPA จบlevel',
    ], axis='columns')

    # ข้อมูล Target
    y = df['GPA จบ']

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

    return branch, model, r_squared, intercept, slope

def pre_model(modelOdject,inputData):
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
        answer = i['model'].predict([inputData])
        answer_mlinear = i['modelMLinear'].predict([inputData])[0]
        
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
