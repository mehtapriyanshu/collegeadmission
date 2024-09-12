from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name= 'home'),
    path('student/<str:id>',views.students,name='student'),
    path('create_student/',views.create_student,name='create_student'),
    path('update_student/<str:id>',views.updatestudent,name='updatestudent'),
    path('deletestudent/<str:id>',views.deletestudent,name='deletestudent'),
    path('createclass/',views.createclass,name = 'createclass'),
    path('printstudent/',views.print_student, name='printstudents'),
    path('deleteclass/<int:id>/',views.delete_class,name= 'deleteclass'),
    path('export/excel/', views.export_to_excel, name='export_to_excel'),
    path('whatsapp-contact/', views.whatsapp_contact, name='whatsapp_contact')
    # path('search', views.search, name='search'),
    # path('student/<str:pk>/fees/', views.student_fees, name='student_fees'),
    # path('create_fee/<str:id>',views.create_fee,name='createfee'),
    # path('autocomplete-search/', views.autocomplete_search, name='autocomplete_search'),

]