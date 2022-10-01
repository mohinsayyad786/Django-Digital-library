

from django.http import HttpResponse
from django.shortcuts import render,redirect 
from django.http import HttpResponse
from libapp.models import WORK,Book_Issue
from libapp.form import RegisterForm 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q






# Create your views here.


def index(request):

    content={}
    user_id=request.user.id
    Q1=Q(is_deleted='N')
    Q2=Q(uid=user_id)
    content['data']=WORK.objects.filter(Q1&Q2)
    return render(request,'index.html',content) 



def create_work(request):

    if request.method=='POST':
        B=request.POST['B']
        At=request.POST['At']
        Pc=request.POST['Pc']
        dt=request.POST['dt']
        user_id=request.user.id
        w1=WORK.objects.create(bookname=B,author=At,publication=Pc,date=dt,uid=user_id,is_deleted='N')
        w1.save()
        return redirect('/')

    else:    
        return render(request,'create_work.html')


def delete(request,rid):
    x=WORK.objects.filter(id=rid)
    x.update(is_deleted='Y')
    return redirect('/')


def edit(request,rid):
    
    if request.method=='POST':

        uB=request.POST['B']
        uAt=request.POST['At']
        uPc=request.POST['Pc']
        udt=request.POST['dt']
        x=WORK.objects.filter(id=rid)
        x.update(bookname=uB,author=uAt,publication=uPc,date=udt)
        return redirect('/')
       
    else:
        content={}
        content['data']=WORK.objects.filter(id=rid)
        return render(request,'editform.html',content)


def book_issue(request):

    if request.method=='POST':
        SN=request.POST['SN']
        BN=request.POST['BN']
        ID=request.POST['ID']
        RD=request.POST['RD']
        BC=request.POST['BC']
        w1=Book_Issue.objects.create(studentname=SN,bookname=BN,issuedate=ID,returndate=RD,charge=BC,is_deleted='N')
        w1.save()
        return redirect('/')

    else:    
        return render(request,'issuebook.html')


def book_issued(request):
    content={}
    content['data']=Book_Issue.objects.filter(is_deleted='N')
    return render(request,'issuedbooks.html',content)

def delete_book(request,rid):
    x=Book_Issue.objects.filter(id=rid)
    x.update(is_deleted='Y')


def ALL_BOOK(request):
    content={}
    content['data']=WORK.objects.filter(is_deleted="N")
    return render(request,'index.html',content)

def DR_APJ(request):
    content={}
    content['data']=WORK.objects.order_by('bookname').filter(author="DR.APJ")
    return render(request,'index.html',content)

'''
def VIVEKANAND(request):
    content={}
    content['data']=WORK.objects.order_by('bookname').filter(author="VIVEKANAND")
    return render(request,'index.html',content)
    '''


def MOHIN(request):
    content={}
    content['data']=WORK.objects.order_by('bookname').filter(author="mohin")
    return render(request,'index.html',content)



def MAHARASHTRA(request):
    content={}
    content['data']=WORK.objects.order_by('publication').filter(publication="MAHARASHTRA")
    return render(request,'index.html',content)

def INDIAN(request):
    content={}
    content['data']=WORK.objects.order_by('publication').filter(publication="INDIAN")
    return render(request,'index.html',content)

def NETFLIX(request):
    content={}
    content['data']=WORK.objects.order_by('publication').filter(publication="netflix")
    return render(request,'index.html',content)


def Register(request):

    if request.method=='POST':

        fm=RegisterForm(request.POST)

        
        if fm.is_valid():
            messages.success(request,'Account Created Successfully,please Login!!!')
            fm.save()

        return redirect('/register')
    else:  
        fm=RegisterForm()
        return render(request,'signup.html',{'form':fm})


def Login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u)
                return redirect('/')

    else:
        fm=AuthenticationForm()

        return render(request,'login.html',{'form':fm})


def getlogonuserid(request):
    user_id=request.user.id
    return render(request,'getloginid.html',{'data':user_id})


def Logout(request):
    logout(request)

    return redirect('/login')




    










    


