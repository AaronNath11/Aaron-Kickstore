from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Aaron Kickstore',
        'name': 'Aaron Nathanael Suhaendi',
        'class': 'PBP B'
    }
    return render(request, "main.html", context)
