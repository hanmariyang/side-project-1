from django.shortcuts import render,redirect
from .models import ReviewModel

# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/review')
    else:
        return redirect('/log-in')
        
def review(request):
    if request.method == 'GET': # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어있는지 확인
        if user: #로그인 한 사용자라면
             return render(request, 'review/review.html')
        else: #로그인이 되어 있지 않다면
             return redirect('/log-in')
    elif request.method == 'POST': #요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_review = ReviewModel()
        my_review.user = user # 모델에 사용자 저장
        my_review.rating = request.POST.get('rating','')
        my_review.image =request.POST.get('image','')
        my_review.purchase_info = request.POST.get('purchase_info','') 
        my_review.product_info =request.POST.get('product_info','')
        my_review.size = request.POST.get('size','')
        my_review.content = request.POST.get('content','')
        my_review.save()
        return redirect('/detail')

def detail(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_review = ReviewModel.objects.all().order_by('-created_at')
            return render(request,'review/detail.html', {'detail':all_review})
        else:
            return redirect('log-in')
    
        
