from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165805',
        'name': 'Anindya Nabila Syifa',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)