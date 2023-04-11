from django.shortcuts import render

# Create your views here.
def fees_django(request):
    '''
    cname = 'Django'
    duration = '6 Months'
    seats = 10
    fees = 5000
    django_details = {'name': cname, 'dur': duration, 'st': seats, 'fe': fees}
    return render(request, 'fees/feesone.html', django_details)
    '''
    # return render(request, 'fees/feesone.html', {'cname': 'Django', 'duration': '6 Months', 'seats': 10, 'fees': 5000})
    django_details = {'cname': 'Django', 'duration': '6 Months', 'seats': 10, 'fees': 5000}
    return render(request, 'fees/feesone.html', context= django_details)

def fees_python(request):
    python_details = {'cname': 'Python', 'duration': '4 Months', 'seats': 10, 'fees': 3000}
    return render(request, 'fees/feesone.html', context= python_details)
    '''
    cname = 'Python'
    duration = '4 Months'
    seats = 20
    fees = 2000
    python_details = {'name': cname, 'dur': duration, 'st': seats, 'fe': fees}
    return render(request, 'fees/courseone.html', python_details)
    '''
    # return render(request, 'fees/courseone.html', {'cname': 'Django', 'duration': '6 Months', 'seats': 10, 'fees': 5000})
   
