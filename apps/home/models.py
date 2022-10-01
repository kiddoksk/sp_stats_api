from django.db import models


class UserDetails(models.Model):
    """
    User Model
    """
    id = models.AutoField(primary_key=True, help_text='Unique Id to identify a user')
    user_name = models.CharField(max_length=255, help_text='Name of the user')
    password = models.CharField(max_length=55, help_text='User Password')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at datetime')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at datetime')

    class Meta:
        db_table = 'user_details'


class StudentDetails(models.Model):
    """
    Student Details Model
    """
    id = models.AutoField(primary_key=True, help_text='Unique ID')
    gender = models.CharField(max_length=10, help_text='Gender of the Student')
    race = models.CharField(max_length=50, help_text='Race/ethnicity of the student')
    parent_education = models.CharField(max_length=50, help_text='Parent Education Level of the student')
    lunch = models.CharField(max_length=255, help_text='Lunch')
    test_preparation_course = models.CharField(max_length=255, help_text='Test Preparation course')
    math_score = models.IntegerField(help_text='Math Score')
    reading_score = models.IntegerField(help_text='Reading Score')
    writing_score = models.IntegerField(help_text='Writing Score')

    class Meta:
        db_table = 'student_details'
