from django.shortcuts import render


def index(request):
    print(request.POST)
    return render(request, 'epp_student/student.html')
