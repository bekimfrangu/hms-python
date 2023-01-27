from django.urls import path
from .views import About, Home, Index, Login, Logout_admin, Index, View_doctor, Delete_doctor, Add_doctor, View_patient, Delete_patient, Add_patient, Add_appointment, View_appointment, Delete_appointment

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('add_doctor/', Add_doctor, name='add_doctor'),
    path('view_patient/', View_patient, name='view_patient'),
    path('add_patient/', Add_patient, name='add_patient'),
    path('view_appointment/', View_appointment, name='view_appointment'),
    path('add_appointment/', Add_appointment, name='add_appointment'),
    path('delete_doctor/?p<int:pid>', Delete_doctor, name='delete_doctor'),
    path('delete_patient/?p<int:pid>', Delete_patient, name='delete_patient'),
    path('delete_appointment/?p<int:pid>', Delete_appointment, name='delete_appointment'),
]
