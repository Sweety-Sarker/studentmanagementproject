from django.shortcuts import render,redirect
from projectApp.models import *
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def homepage(req):
    data=projectModel.objects.filter(created_by=req.user)
    context={
        'data':data
    }
    return render (req,'homepage.html',context)



def registerpage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        student_name=req.POST.get('student_name')
        student_id=req.POST.get('student_id')

        if password==confirm_password:
            userModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                student_name=student_name,
                student_id=student_id,
            )
            return redirect('loginpage')
    return render (req,'registerpage.html')




def loginpage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
        return redirect('homepage')
    return render (req,'loginpage.html')



def logoutpage(req):
    logout(req)
    return redirect('loginpage')



# @login_required
def addlist(req):
    if req.method == 'POST':
        project_name=req.POST.get('project_name')
        project_description=req.POST.get('project_description')
        deadline=req.POST.get('deadline')
        project_status=req.POST.get('project_status')

        data=projectModel(
            created_by=req.user,
            project_name=project_name,
            project_description=project_description,
            deadline=deadline,
            project_status=project_status,
        )
        data.save()
        return redirect('projectlist')
    return render(req,'addlist.html')



# @login_required
def projectlist(req):
    data=projectModel.objects.filter(created_by=req.user)
    context={
        'data':data
    }
    return render(req,'projectlist.html',context)



# @login_required
def editpage(req,id):
    data=projectModel.objects.get(id=id)
    
    context={
        'data':data
    }
    if req.method == 'POST':
        data.project_name=req.POST.get('project_name')
        data.project_description=req.POST.get('project_description')
        data.deadline=req.POST.get('deadline')
        data.project_status=req.POST.get('project_status')
        data.save()
        return redirect('projectlist')
    return render(req,'editpage.html',context)



# @login_required
def deletepage(req,id):
    data=projectModel.objects.get(id=id).delete()
    return redirect('projectlist')



# @login_required
def viewpage(req,id):
    data=projectModel.objects.get(id=id)
    context={
        'data':data
    }
    return render(req,'viewpage.html',context)



# @login_required
def stategechange(req,id):
    data=projectModel.objects.get(id=id)

    if data.project_status == 'NotStarted':

        data.project_status = 'InProgress'

    elif data.project_status == 'InProgress':
          
          data.project_status = 'Completed'

    data.save()
    return redirect('projectlist')

