import csv

from django.conf import settings

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import UserDetails, StudentDetails
from .serializers import UserDetailSerializer
from .utils import get_median_value, get_average_value, get_sum_value

ROOT_DIR = str(settings.BASE_DIR)

DB_PATH = ROOT_DIR + '/db.sqlite3'
CSV_PATH = ROOT_DIR + '/student_details.csv'


class UserDetailsView(generics.ListCreateAPIView):
    """
    User Details View
    """

    def post(self, request, **kwargs):
        """
        Post of User Details
        """
        try:
            user_name = request.data.get('user_name')
            password = request.data.get('password')

            user_details = UserDetails.objects.filter(user_name=user_name, password=password).first()

            if not user_details:
                user_details = UserDetails.objects.create(
                    user_name=user_name,
                    password=password
                )
                user_details.save()

            return Response(
                data=UserDetailSerializer(user_details).data,
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    'message': 'Invalid Login Attempt, Please try again with correct user_name and password'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class StudentDetailsView(generics.ListCreateAPIView):
    """
    Student Details View
    """
    def post(self, request, **kwargs):
        """
        Insert student details to DB from CSV file
        """
        with open(CSV_PATH) as f:
            student_details = csv.reader(f)
            next(student_details)
            for row in student_details:
                StudentDetails.objects.create(
                    gender=row[0],
                    race=row[1],
                    parent_education=row[2],
                    lunch=row[3],
                    test_preparation_course=row[4],
                    math_score=row[5],
                    reading_score=row[6],
                    writing_score=row[7]
                )

        return Response(
            {
                'message': 'Student Details inserted'
            },
            status=status.HTTP_200_OK
        )

    def get(self, request, *args, **kwargs):
        """
        Get all students data
        """
        try:
            gender = self.request.query_params.get('gender', None)
            race = self.request.query_params.get('race', None)
            parent_education = self.request.query_params.get('parent_education', None)
            lunch = self.request.query_params.get('lunch', None)
            test_preparation_course = self.request.query_params.get('test_preparation_course', None)

            filters = {}

            if gender:
                filters['gender'] = gender

            if race:
                filters['race'] = race

            if parent_education:
                filters['parent_education'] = parent_education

            if lunch:
                filters['lunch'] = lunch

            if test_preparation_course:
                filters['test_preparation_course'] = test_preparation_course

            filtered_data = StudentDetails.objects.filter(**filters).order_by('id')

            # get math stats
            math_median = get_median_value(filtered_data, 'math_score')
            math_average = get_average_value(filtered_data, 'math_score')
            math_sum = get_sum_value(filtered_data, 'math_score')

            # get reading stats
            reading_median = get_median_value(filtered_data, 'reading_score')
            reading_average = get_average_value(filtered_data, 'reading_score')
            reading_sum = get_sum_value(filtered_data, 'reading_score')

            # get writing stats
            writing_median = get_median_value(filtered_data, 'writing_score')
            writing_average = get_average_value(filtered_data, 'writing_score')
            writing_sum = get_sum_value(filtered_data, 'writing_score')

            response = {
                'math_average': math_average,
                'math_median': math_median,
                'math_sum': math_sum,
                'reading_sum': reading_sum,
                'reading_average': reading_average,
                'reading_median': reading_median,
                'writing_average': writing_average,
                'writing_median': writing_median,
                'writing_sum': writing_sum
            }

            return Response(
                data=response,
                status=status.HTTP_200_OK
            )

        except StudentDetails.DoesNotExist:
            return Response(
                {
                    'message': 'Student Details does not exist'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
