from django.shortcuts import render
from crud.models import Student

# Create your views here.
def student(request):
    #    students = [
    #    {"name": "Nabs", "age": 25, "email": "nabs24@email.com", "address": "MNR"},
    #    {"name": "Navya", "age": 18, "email": "navya@email.com", "address": "MNR"},
    #    {"name": "Rolex", "age": 20, "email": "rolex21@email.com", "address": "MNR"},
    #    {"name": "Nabraj...", "age": 28, "email": "nabs@email.com", "address": "MNR"},
    # ]
    students=Student.objects.all()
    return render(request, template_name="commons/student.html",  context={"students": students})
   
   
   
def classroom(request):
    classrooms = [
        {"name":"One", "section": "A"},
        {"name":"Two", "section": "B"},
        {"name":"Three", "section": "B"},
        {"name":"Four", "section": "A"},
        {"name":"Five", "section": "A"},
    ]
    return render(request, "commons/classroom.html", {"classrooms": classrooms})



def not_found_404(r, *args, **kwargs):
    return render(r, template_name='404_not_found.html')