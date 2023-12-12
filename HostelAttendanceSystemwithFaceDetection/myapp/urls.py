
from django.contrib import admin
from django.urls import path,include

from myapp import views

urlpatterns = [
    path('login/', views.login),

    path('add_student/',views.add_student),
    path('change_password/',views.change_password),
    path('edit_student/<id>',views.edit_student),
    path('view_attendance/',views.view_attendance),
    path('view_details/',views.view_details),
    path('delete_student/<id>',views.delete_student),
    path('home/',views.home),
    path('search/',views.search),


    path('login_post/',views.login_post),
    path('add_student_post/',views.add_student_post),
    path('change_password_post/',views.change_password_post),
    path('edit_student_post/',views.edit_student_post),
    path('view_attendance_post/',views.view_attendance_post),
    path('view_details_post/',views.view_details_post),



]
