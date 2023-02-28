from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm

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
    if request.method=="GET":
        result=request.GET.get('output')
    return render(request,"contact.html", {'result': result })

def userform(request):
    fn=usersForm()
    finalans=0
    data = {'form':fn}
    try:
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        finalans=n1+n2
        data={
            'from':fn,
            'output':finalans
        }
        url='/contact?output={}'.format(finalans)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform.html",data)


def submitform(request):
    data = {}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('name'))
            n2=int(request.POST.get('email'))
            n3=int(request.POST.get('message'))
            data={
                'n1':n1,
                'n2':n2,
                'n3':n3
            }
            #return render(request,'submitform',data)
            return HttpResponse(n2)
    except:
        pass
    #return render(request,"submitform.html",data)

def submit(request):
    data= {}
    try:
        if request.method=="POST":
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            return HttpResponse(data)
    except:
        pass


