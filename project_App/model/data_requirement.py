import pandas as pd 
import numpy as np 
from django.db import connection
from project_App.models import *

# คำนวณเกรดจาก input
def calculat_gpa(temp):
    req_array = []
    data = []
    units = []

    inputs = {k: v for k, v in temp.items() if v != ''}
    cursor  =  connection.cursor()
    cursor .execute('SELECT course_unit,course_name_en FROM mrs_database.course')
    result = cursor.fetchall()
    for item in result: 
        item = list(item)
        item[1] =item[1].lower()  #จัดรูปให้เป็นตัวเล็ก
        item[1] = item[1].replace(" ", "_")  #จัดรูปให้เป็นตัวเล็ก
        req_array.append(item)
        
    for i in req_array:
        for j in inputs:
            if (i[1] == j):
                data.append(float(i[0][0])  * float(inputs[j]))
                units.append(float(i[0][0]))
    input_gpa = round(sum(data) / sum(units), 2)
    # print(input_gpa)
    return input_gpa

# จัดรูปแบบ input เพื่อไปจัดความต้องการ 
def change_input(temp):
    data= temp
    dictionary={} #เก็บแบบform dictionary 
    course_id=[]    #เก็บ course_id
    course_name=[]  #เก็บชื่อวิชา
    grade=[]        #เก็บ grade แต่ละวิชา
    input_studant=[]     #เลือกเก็บขอมูลที่ใช้จริง
    
    # สร้าง course_id
    for d in range(1, 17):
        course_id.append(d)

    # แยกข้อมูล course_name แต่ละวิชา และทำให้เป็นตัวพิมพ์เล็ก
    # # แยก grade แต่ละวิชา
    for d in data:
        course_name.append(d)    
        grade.append(data[d])
    
    # รวมข้อมูลที่แยกออก เป็น dictionary
    val = range(len(course_name))
    for i in val :
        dictionary[i] = {
        'course_id':course_id[i],
        'course_name':course_name[i],
        'grade':grade[i]
        }
    
    # คัดเอา key ของแต่ละ dictionary  ออก
    for key, value in dictionary.items():
        temp = value
        input_studant.append(temp)

    return input_studant

# SELECT ข้อมูล TABEL datastudent ของ เนย
def get_data_student_df():
    dfs = pd.read_csv("C:/Users/picha/Desktop/code jupyter/data_student1 .csv")
    dfs.columns = dfs.columns.str.replace(' ','_')
    student_df = dfs.rename(columns=str.lower)
    return student_df
# SELECT DATABASE ข้อมูลความความต้องการของสาขา
def get_major_req_df():
    majors_req_array = []
    
    mycursor = connection.cursor()
    mycursor.execute("""
        SELECT m.id AS major_id ,
            m.name, c.id AS course_id ,
            c.course_name_en ,
            d.id AS department_id ,
            d.name AS department_name
        FROM majors_requirement mr 
        LEFT JOIN majors m 
            ON mr.major_id = m.id
        LEFT JOIN course c
            ON mr.course_id = c.id
        LEFT JOIN departments d
            ON mr.department_id = d.id
        WHERE mr.status = 1;
                    """)
    select_result = mycursor.fetchall()
    for item in select_result: 
        if(item[3] != None and item[2] != None):
            item = list(item)
            item[3] = item[3].lower()   #จัดรูปให้เป็นตัวเล็ก
            item[3] = item[3].replace(" ", "_") # แทนที่ " " เป็น "_"
            majors_req_array.append(list(item))
        else :
            majors_req_array.append(list(item))

    df = pd.DataFrame(
        majors_req_array,
        columns=['major_id','major_name','course_id','course_name_en','department_id','department_name'])
    return df

def data_set_df(input, input_gpa):
    # ดึงข้อมูล Database student
    student_df = get_data_student_df()
    major_req_df = get_major_req_df()


    input_predict = []     # input สำหรับการทำนาย
    failed_course = []     # list เก็บวิชาที่ F
    majors_not_pass = []   # list เก็บสาขาที่ไม่ผ่าน
    majors_pass = []       # list เก็บสาขาที่ผ่าน

    # ลบ col วิชาที่ F
    for item in input:
        if item['grade'] == 0.0 or item['grade'] ==  '':
            student_df = student_df.drop(columns=[item['course_name']], axis=0)
            failed_course.append(item['course_name'])
        else:
            input_predict.append(item['grade'])
    input_predict.append(input_gpa)
    
    print("วิชาที่ F",failed_course)
    print("input ที่วิชาที่นำมาทำนาย",input_predict)

    # หาสาขาที่ต้อง filter
    if(len(failed_course)): 
        for item in failed_course:
            df = major_req_df.loc[(major_req_df['course_name_en']==item),['major_name']]
            majors_not_pass.extend(df['major_name'].values.tolist()) # pull เก็บสาขาที่ไม่ผ่าน
    df = major_req_df[["major_name"]]
    majors_pass.extend(df['major_name'].values.tolist()) # pull เก็บสาขาที่ผ่าน
    
    majors_not_pass = np.unique(np.array(majors_not_pass)).tolist()
    majors_pass = np.unique(np.array(majors_pass)).tolist()
    
    for item in majors_not_pass:
        majors_pass.remove(item)

    print("สาขาที่ไม่นำมาทำนาย :",majors_not_pass)
    print("สาขาที่นำมาทำนาย :",majors_pass)

    student_df = student_df.loc[student_df['major_name'].isin(majors_pass)]
    student_df = student_df.reset_index(drop=True)
    
    # drop col ที่ไม่ใช่
    student_df = student_df.drop(columns=[
        'student_id', 
        'department_id',
        'department_name',
        'major_id',
        # 'major_name',
        'year_of_study',
    ])

    # จัดรูป GPX เพิ่ม col GPAX_char
    grade = []
    for value in student_df['gpax']:
        if value >= 2.00 and value <= 2.50 :
            grade.append('L')
        elif value >= 2.51 and value <= 3.25 :
            grade.append('M')
        elif value >= 3.26 and value <= 4.00 :
            grade.append('H')
    student_df['GPAX_char'] = grade

    # return
    return input_predict, student_df, majors_pass
