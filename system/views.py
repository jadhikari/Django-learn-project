from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # data={
    #     'title':'Home Page',
    #     'body' : 'Welcome to home page of Manoj',
    #     'list' : ['Java','PHP','Djanjo'],
    #     'students' : [
    #         {'name':'manoj','phone' : '989898998'},
    #         {'name':'jonam','phone' : '121251255'}
    #     ]
    #  }
    #return render(request,"index.html",data)
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def userform(request):
    # finalans=0
    # try:
    #     n1=int(request.GET['num1'])
    #     n2=int(request.GET['num2'])
    #     finalans=n1+n2
    # except:
    #     pass
    # return render(request,"userform.html",{'output':finalans})
    finalans=0
    data = {}
    try:
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        finalans=n1+n2
        data={
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
    except:
        pass
    return render(request,"userform.html",data)
