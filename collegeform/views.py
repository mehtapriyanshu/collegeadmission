from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student , Class
from .forms import collegedetail,Standard
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import JsonResponse
from openpyxl import Workbook

import csv
  
# Create your views here.


def home(request):
    q=  request.GET.get('q') if request.GET.get('q')!=None else ''
    Students = Student.objects.filter(Q(Classs__name__icontains=q)|Q(name__icontains=q)|Q(id__contains=q)|Q(fathername__icontains=q))
    student_count = Students.count()
    Classs = Class.objects.all()
    context = {'Studentss':Students,'Classs':Classs,'student_count':student_count}
    return render(request,'home.html',context)
    



def create_student(request):
    form = collegedetail()
    if request.method == 'POST':
        form = collegedetail(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = collegedetail()
    return render(request,'create_student.html',{'form':form})


def updatestudent(request,id):
    student = Student.objects.get(pk=id)
    form = collegedetail(instance = student)
    if request.method == 'POST':
        form = collegedetail(request.POST,instance= student)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'create_student.html',context)

def students(request,id): 
    student = Student.objects.get(pk=id)
    context = {'student':student}
    return render(request,'student.html',context)

def deletestudent(request,id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request,'delete.html',{'Name':student})



def createclass(request):
    form = Standard()
    
    if request.method == 'POST':
        form = Standard(request.POST)

        if form.is_valid():
            class_name = form.cleaned_data.get('name')
            if Class.objects.filter(name=class_name).exists():
                return render(request, 'create_class.html', {'form': form, 'error': 'Class already exists.'})
            else:
                form.save()
                return redirect('home')
    else:
        form = Standard()
    return render(request,'create_class.html',{'form':form})


def delete_class(request, id):
    classs = get_object_or_404(Class, id=id)
    
    if  Student.objects.filter(Classs = classs).exists():
        return render(request, 'classdelete.html', {'Classs': classs, 'error': 'Cannot delete class because student are enrolled this class.'})
    elif request.method == 'POST':
        classs.delete()
        return redirect('home')
    return render(request, 'classdelete.html', {'Classs': classs})




def print_student(request):
    # student = Student.objects.all()
    classs = request.GET.get('Class')
    if classs :
        student = Student.objects.filter(classs__name= classs)
    else:
        student = Student.objects.all()
    return render(request,'printstudent.html',{'students':student,'classs':classs})



def export_to_excel(request):
    response = HttpResponse(content_type= 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Studentid','name','class','fathername'])
    for student in Student.objects.all().values_list('id','name','Classs','fathername'):
        writer.writerow(student)

    response['Content-Disposition'] = 'attachment; filename="studentlist.csv" '
    return response

def whatsapp_contact(request):
    return render(request,'whatsappcontact.html')

























































































































































































































































































































































    # wb = Workbook()
    # ws = wb.active
    # ws.title= "Students"

    # headers = ["ID","Name","Class","fathername"]
    # ws.append(headers)

    # students = Student.objects.all()
    # for student in students:
    #     student_class = str(student.Classs) if student.Classs else ''
    #     ws.append([student.id,student.name,student.Classs,student.fathername])
    # response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    # response['Content-Disposition'] = 'attachment; filename=students.xlsx'
    # wb.save(response)
    # return response

# @csrf_exempt
# def autocomplete_search(request):
#     if 'term' in request.GET:
#         query = request.GET.get('term')
#         students = Student.objects.filter(name__icontains=query)[:10]  # Adjust the field as needed
#         suggestions = list(students.values_list('name', flat=True))  # Return only the names
#         return JsonResponse(suggestions, safe=False)
#     return JsonResponse([], safe=False)

# def search(request):
#     q = request.GET.get('q', '')
#     results = Student.objects.filter(Q(Classs__name__icontains=q)|Q(name__icontains=q)|Q(id__contains=q)|Q(fathername__icontains=q)) if q else Student.objects.all()
#     return render(request, 'search.html', {'results': results})

# def search_student(request):
#     student = request.GET.get('student')
#     payload= []
#     if student:
#         student = Student.objects.filter(name__icontains=student)

#         for sstudent in student:
#             payload.append(student.name)

#     return JsonResponse({'status':200,'data':payload})


# def create_fee(request, id):
#     form= fees()
#     if request.method == 'POST':
#         form = fees(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_fees', pk=id)
#     else:
#         form = fees()
#     return render(request,'create_fee.html',{'form':form})
#     # student = get_object_or_404(Student, pk=id)  # Always use student.id to uniquely identify
#     # if request.method == 'POST':
#     #     total_fees = request.POST.get('total_fees')
#     #     paid_fees = request.POST.get('paid_fees')
#     #     # Create the fees record associated with the student
#     #     Fees.objects.create(student=student, total_fees=total_fees, paid_fees=paid_fees)
#     #     return redirect('student_fees', pk=id)  # Redirect to the student fees page
#     # return render(request, 'create_fee.html', {'student': student})


# def student_fees(request,pk):
#     student = get_object_or_404(Student, pk=pk)
#     fees = Fees.objects.filter(student=student)
    
#     return render(request, 'studentfees.html', {'student': student, 'fees': fees})