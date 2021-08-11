from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


#Adding Function and Displays
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['position']
            reg = User(name=nm, email=em, position=ps)
            reg.save()
            fm = StudentRegistration
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'addandshow.html',{'form':fm,'stu':stud})



#Deleting Function 
def delete(request, id):
    if request.method == 'POST':
        dlt =  User.objects.get(pk=id)
        dlt.delete()
        return HttpResponseRedirect('/')


#Updating Function 
def update(request,id):
    if request.method == 'POST':
        upd = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=upd)
        if fm.is_valid():
            fm.save()
    else:
        upd = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=upd)  
    return render(request, 'updatestudent.html',{'form': fm})

