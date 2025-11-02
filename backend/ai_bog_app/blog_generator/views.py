from django.shortcuts import render

# CreatE your views here
def index(request):
    return render(request, 'index.html')