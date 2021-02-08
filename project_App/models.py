# from django.db import models,connection

# # Create your models here.
# class Course(models.Model):
#     course_code = models.CharField(max_length=10, blank=True, null=True)    
#     course_unit = models.CharField(max_length=10, blank=True, null=True)    
#     course_name_th = models.CharField(max_length=100, blank=True, null=True)
#     course_name_en = models.CharField(max_length=100, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'course'


# class Departments(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=191)   
#     status = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'departments'


# class FailedJobs(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     connection = models.TextField()
#     queue = models.TextField()
#     payload = models.TextField()
#     exception = models.TextField()
#     failed_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'failed_jobs'


# class Grades(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     gradename = models.CharField(db_column='gradeName', max_length=3)  # Field name made lowercase.
#     gradenumber = models.FloatField(db_column='gradeNumber', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'grades'


# class Majors(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=191)
#     department_id = models.IntegerField()
#     status = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'majors'


# class MajorsRequirement(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     major_id = models.IntegerField(blank=True, null=True)
#     course_id = models.IntegerField(blank=True, null=True)
#     department_id = models.IntegerField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'majors_requirement'



# # class DataStudent(models.Model):
# #     student_id = models.CharField(primary_key=True, max_length=14)
# #     gpax = models.DecimalField(db_column='GPAX', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
# #     department_id = models.IntegerField(blank=True, null=True)
# #     department_name = models.CharField(max_length=41, blank=True, null=True)
# #     major_id = models.IntegerField(blank=True, null=True)
# #     major_name = models.CharField(max_length=58, blank=True, null=True)
# #     year_of_study = models.IntegerField(blank=True, null=True)
# #     society_and_environment = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     english_for_communication_1 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     recreation = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     engineering_drawing = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     engineering_materials = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     calculus_for_engineers_1 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     physics_for_engineers_1 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     physics_laboratory_for_engineers_1 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     engineering_mechanics = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     basic_engineering_training = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     computer_programming = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     calculus_for_engineers_2 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     chemistry_for_engineers = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     chemistry_laboratory_for_engineers = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     physics_for_engineers_2 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     physics_laboratory_for_engineers_2 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
# #     gpay1s2 = models.DecimalField(db_column='GPAY1S2', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

# #     class Meta:
# #         managed = False
# #         db_table = 'data_student'