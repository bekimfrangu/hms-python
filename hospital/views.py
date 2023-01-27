from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment

# Create your views here.
def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1
    d1 = {'d':d, 'p':p, 'a':a}
    return render(request, 'index.html', d1)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('admin_login')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html',d)

def Delete_doctor(request, pid):
    if not request.user.is_staff:
        return('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(Name=n, mobile=m, special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_doctor.html', d)

    
def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request, 'view_patient.html',d)
    
def Delete_patient(request, pid):
    if not request.user.is_staff:
        return('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def Add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        add = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=add)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_patient.html', d)

def Add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    pat1 = Patient.objects.all()
    doc1 = Doctor.objects.all()
    if request.method == 'POST':
        dn = request.POST['doctor']
        pn = request.POST['patient']
        dt = request.POST['date']
        t = request.POST['time']
        doc = Doctor.objects.filter(Name=dn).first()
        pat = Patient.objects.filter(name=pn).first()
        try:
            Appointment.objects.create(doctor=doc, patient=pat, date=dt, time=t)
            error = "no"
        except:
            error = "yes"
    d = {'error':error, 'doc':doc1, 'pat':pat1}
    return render(request, 'add_appointment.html', d)

def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appts = Appointment.objects.all()
    d = {'appts':appts}
    return render(request, 'view_appointment.html',d)
    
def Delete_appointment(request, pid):
    if not request.user.is_staff:
        return('login')
    appoint = Appointment.objects.get(id=pid)
    appoint.delete()
    return redirect('view_appointment')
