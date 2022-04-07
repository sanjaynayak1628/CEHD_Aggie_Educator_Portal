from django.shortcuts import render

# Create your views here.

def index(request):
    print(request.POST)
    return render(request, 'epp_student/student.html')
