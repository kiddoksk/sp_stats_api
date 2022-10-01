from django.urls import path

from .views import UserDetailsView, StudentDetailsView

urlpatterns = [
    path('user_details/', UserDetailsView.as_view(), name='user-details'),
    path('student_details/', StudentDetailsView.as_view(), name='student-details')
]

https://enigmatic-temple-75763.herokuapp.com/api/user_details/

https://enigmatic-temple-75763.herokuapp.com/api/student_details/?gender=male&race=group%20B&parent_education=high%20school&lunch=standard&test_preparation_course=none
