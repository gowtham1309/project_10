from django.shortcuts import render

# Create your views here.
def pg(request):
    d={'name':'akshaya','floor':3}
    return render(request,'pg.html',context=d)
