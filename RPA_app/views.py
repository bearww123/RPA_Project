from django.shortcuts import render

# 메인 페이지
def home(request):
    return render(request, 'index.html')
