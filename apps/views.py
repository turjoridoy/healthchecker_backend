from django.shortcuts import render


def say_day(request):
    return render(request, 'day.html', {'name': 'Md. Mosharaf Hossain'})


