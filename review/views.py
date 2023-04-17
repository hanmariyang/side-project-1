from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/review')
    else:
        return redirect('/log-in')
    
def review(request):
    if request.method == 'GET':
        user = request.user.is_authenticated 
        if user:
            return render(request, 'review/home.html')
        else:
            return redirect('/log-in')