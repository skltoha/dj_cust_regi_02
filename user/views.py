from django.shortcuts import render

# Create your views here.

def profile(request):
    if request == 'POST':
        pass
    else:
        return render(request, 'userdetails.html')