from django.shortcuts import render,redirect
# Create your views here.
from django.template import loader
import datetime
from django.http import HttpResponse,HttpResponseNotFound
#from django.views.decorators.http import require_http_methods
#@require_http_methods(["GET"])

from gowapp.form import StudForm
from gowapp.form import uploadform
from gowapp.static.upload.functions import handle_uploaded_file
from gowapp.form import EmppForm  # validation auto - purpose



def EmppFun(request):  # auto validation purpose
    if request.method == 'POST':
        e1=EmppForm(request.POST,request.FILES)
        if e1.is_valid():            
            return HttpResponse("page valid success")
        else:
            return HttpResponse("page In - valid ")
            #return redirect('/uploadfun')
            '''
            try:
                #return redirect('/')
                return HttpResponse("page valid success")
            except:
                return HttpResponse("page invalid error")
                #pass
                '''
    else:
        e1=EmppForm()
        return render(request,"pgm9.html",{'form':e1})                                 
    #return render(request,"pgm9.html",{'form':e1})                                 
        

def uploadfun(request):
    if request.method=='POST':
        obj=uploadform(request.POST,request.FILES)
        if obj.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File Uploaded Successfully")
    else:
        obj=uploadform()
        return render(request,"pgm8.html",{'form':obj})                                 

def modelfun(request):
    stu=StudForm()
    return render(request,'pgm7.html',{'form':stu})  # using model

def loadcss(request):
    #return render(request,'pgm6.html')
    return render(request,'pgm10.html')

def loadjsrun(request):
    return render(request,'pgm5.html')

def loadjsfun(request):
    return render(request,'pgm4.html')

def stimgfun(request):
    return render(request,'pgm3.html')

def varfun(request):
    tem=loader.get_template("pgm2.html")
    mydetails={"rno":1001,
          "name":"gowthaman",
          "mark":100
          }
    return HttpResponse(tem.render(mydetails))

def temfun(request):
#    template=loader.get_template("pgm1.html")
    template=loader.get_template("pgm10.html")
    return HttpResponse(template.render())
    

def show(request):
    return HttpResponse(" this is http request method get ")

def index(request):
    a=10
    if a==1:
        return HttpResponseNotFound("<h1> Page is not Found </h1>")
    else:
        return HttpResponse("<h1> Page Valid </h1>")


    '''
    now=datetime.datetime.now()
    html="<html><body>Today Date & time: %s</body></html>"%now
    return HttpResponse(html)
    '''
