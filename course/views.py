from django.shortcuts import render

# Create your views here.
def learn_django(request):
    cname = 'Django'
    duration = '6 Months'
    seats = 10
    django_details = {'name': cname, 'duration': duration, 'seats': seats}
    # return render(request, 'course/courseone.html', django_details)
    # return render(request, 'course/courseone.html', {'cname': 'Django', 'duration': '6 Months', 'seats': 10})
    return render(request, 'course/courseone.html', context= django_details)

def learn_python(request):
    cname = 'Python'
    duration = '4 Months'
    seats = 20
    python_details = {'name': cname, 'duration': duration, 'seats': seats}
    # return render(request, 'course/courseone.html', python_details)
    # return render(request, 'course/courseone.html', {'cname': 'Python', 'duration': '4 Months', 'seats': 20})
    return render(request, 'course/courseone.html', context= python_details)
