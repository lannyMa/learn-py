from django.shortcuts import render

# Create your views here.


def home(request):
    string="无法可修饰的一双手..."
    # names=[]
    nums = map(str,range(100))
    txl={
        'name':'张雨生',
        'age':22,
        'jobs':'歌手'
    }
    return render(request,'home.html',{ 'nums':nums })