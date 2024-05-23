from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    query_strings = request.GET 
    name = query_strings.get("name")
    print(name)
    print(request.scheme)
    print(request.method)
    print(request.user)
    print(request.get_full_path())
    return HttpResponse(f"Hello world. I am {name}")

def home_detail(request,id):
    return HttpResponse(f'<h1>My home id is {id}')

def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")

def test(request):
    return render(request, template_name="myapp/test.html")

def root_page(request):
    return render(request, template_name="myapp/root_page.html")

def learning_context(request):
    student = {"name": "Nabraj", "age": 21, "email": "nabrajmadai21@email.com", "address": "MNR"}
    students = [
       {"name": "Nabs", "age": 25, "email": "nabs24@email.com", "address": "MNR"},
       {"name": "Navya", "age": 18, "email": "navya@email.com", "address": "MNR"},
       {"name": "Rolex", "age": 20, "email": "rolex21@email.com", "address": "MNR"},
       {"name": "Nabraj...", "age": 28, "email": "nabs@email.com", "address": "MNR"},
    ]
    return render(request, template_name="myapp/learning_context.html", context={"students": students, "student": student})

def using_bootstrap(request):
    students = [
       {"name": "Nabs", "age": 25, "email": "nabs24@email.com", "address": "MNR"},
       {"name": "Navya", "age": 18, "email": "navya@email.com", "address": "MNR"},
       {"name": "Rolex", "age": 20, "email": "rolex21@email.com", "address": "MNR"},
       {"name": "Nabraj...", "age": 28, "email": "nabs@email.com", "address": "MNR"},
    ]
    return render(request, template_name="myapp/using_bs.html", context={"student": students })