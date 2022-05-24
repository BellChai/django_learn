from django.http import HttpResponse
from django.shortcuts import render

def runoob(request):
    context = {}
    context['name'] = 'Chai Yihan'
    return render(request, 'runoob.html', context)
    # return HttpResponse("Hello world!!!")