from django.db import models

# Create your models here.
class Datastudent(models.Model):
    idstu                           = models.CharField(db_column='รหัสนักศึกษา', primary_key=True, max_length=14) 
    gpa_end                         = models.DecimalField(db_column='GPA จบ', max_digits=3, decimal_places=2, blank=True, null=True)  
    id_departments                  = models.IntegerField(blank=True, null=True)
    Department                      = models.CharField(db_column='ภาควิชา', max_length=41, blank=True, null=True)  
    id_branch                       = models.IntegerField(blank=True, null=True)
    Branch_code                     = models.IntegerField(db_column='รหัสสาขา', blank=True, null=True)  
    branch                          = models.CharField(db_column='สาขาวิชา', max_length=58, blank=True, null=True)  
    year                            = models.IntegerField(db_column='ปีเข้าศึกษา', blank=True, null=True) 
    society_and_environment         = models.DecimalField(db_column='Society and Environment', max_digits=2, decimal_places=1, blank=True, null=True)  
    english_1                       = models.DecimalField(db_column='English for Communication 1', max_digits=2, decimal_places=1, blank=True, null=True)  
    recreation                      = models.DecimalField(db_column='Recreation', max_digits=2, decimal_places=1, blank=True, null=True) 
    engineering_drawing             = models.DecimalField(db_column='Engineering Drawing', max_digits=2, decimal_places=1, blank=True, null=True)  
    engineering_materials           = models.DecimalField(db_column='Engineering Materials', max_digits=2, decimal_places=1, blank=True, null=True) 
    calculus_1                      = models.DecimalField(db_column='Calculus for Engineers 1', max_digits=2, decimal_places=1, blank=True, null=True)  
    physics_1                       = models.DecimalField(db_column='Physics for Engineers 1', max_digits=2, decimal_places=1, blank=True, null=True) 
    physics_lab_1                   = models.DecimalField(db_column='Physics Laboratory for Engineers 1', max_digits=2, decimal_places=1, blank=True, null=True)  
    engineering_mechanics           = models.DecimalField(db_column='Engineering Mechanics', max_digits=2, decimal_places=1, blank=True, null=True) 
    basic_engineering_training      = models.DecimalField(db_column='Basic Engineering Training', max_digits=2, decimal_places=1, blank=True, null=True)  
    computer_programming            = models.DecimalField(db_column='Computer Programming', max_digits=2, decimal_places=1, blank=True, null=True)  
    calculus_2                      = models.DecimalField(db_column='Calculus for Engineers 2', max_digits=2, decimal_places=1, blank=True, null=True)  
    chemistry                       = models.DecimalField(db_column='Chemistry for Engineers', max_digits=2, decimal_places=1, blank=True, null=True)  
    chemistry_lab                   = models.DecimalField(db_column='Chemistry Laboratory for Engineers', max_digits=2, decimal_places=1, blank=True, null=True)  
    physics_2                       = models.DecimalField(db_column='Physics for Engineers 2', max_digits=2, decimal_places=1, blank=True, null=True)  
    physics_lab2                    = models.DecimalField(db_column='Physics Laboratory for Engineers 2', max_digits=2, decimal_places=1, blank=True, null=True)  
    year_1_semester_1               = models.DecimalField(db_column='Year 1,Semester 1', max_digits=3, decimal_places=2, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'datastudent'

