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
        return render(request, 'review/home.html')