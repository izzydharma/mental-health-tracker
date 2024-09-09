from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306256425',
        'name': 'Made Izzy Prema Dharma',
        'class': 'KKI'
    }

    return render(request, "main.html", context)    
    