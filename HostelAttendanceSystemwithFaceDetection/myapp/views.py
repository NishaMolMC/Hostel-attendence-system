from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,"login.html")


def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    lobj=Login.objects.filter(Username=username,Password=password)
    if lobj.exists():
        lobjj=Login.objects.get(Username=username,Password=password)
        request.session['lid'] = lobjj.id
        request.session['log']="lin"

        if lobjj.type == "admin":

            return HttpResponse('''<script>alert("Login Successful");window.location='/myapp/home/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid User");window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid User");window.location='/myapp/login/'</script>''')


def add_student(request):
    if request.session["log"]=="lin":
        return render(request,"Addstdnt.html")
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')


def add_student_post(request):
    if request.session["log"]=="lin":

        Name=request.POST['textfield']
        Place=request.POST['textfield2']
        PostOffice = request.POST['textfield3']
        Pincode = request.POST['textfield4']
        District = request.POST['textfield5']
        Email = request.POST['textfield6']
        PhoneNumber = request.POST['textfield7']
        ParentName = request.POST['textfield8']
        Parentphonenumber = request.POST['textfield9']
        Department = request.POST['textfield10']
        AdmissionYear = request.POST['textfield11']
        Photo = request.FILES['fileField']



        fs=FileSystemStorage()
        date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
        fn=fs.save(date,Photo)
        path=fs.url(date)

        # lobj=Login()
        # lobj.Username=Email
        # lobj.Password=Email

        sobj=Student()
        sobj.Name=Name
        sobj.Place=Place
        sobj.Post=PostOffice
        sobj.Pin=Pincode
        sobj.District=District
        sobj.Email=Email
        sobj.Phone=PhoneNumber
        sobj.Parentname=ParentName
        sobj.Parentphonenumber=Parentphonenumber
        sobj.Department = Department
        sobj.AdmissionYear=AdmissionYear
        sobj.Photo=path
        sobj.save()
        return HttpResponse('''<script>alert("Registration Successfull");window.location='/myapp/add_student/'</script>''')
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')

def change_password(request):
    if request.session["log"] == "lin":
        return render(request,"changepassword.html")
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')


def change_password_post(request):
    if request.session["log"] == "lin":

        CurrentPassword=request.POST['textfield']
        NewPassword=request.POST['textfield2']
        ConfirmPassword = request.POST['textfield3']
        ob=Login.objects.filter(Password=CurrentPassword,id=request.session['lid'])
        if ob.exists():
            ob1 = Login.objects.get(Password=CurrentPassword, id=request.session['lid'])
            if NewPassword==ConfirmPassword:
                ob1.Password=NewPassword
                ob1.save()
                return HttpResponse(
                    '''<script>alert("Password Changed");window.location='/myapp/login/'</script>''')
            else:
                return HttpResponse(
                    '''<script>alert("Password doesnt Match");window.location='/myapp/change_password/'</script>''')
        else:
            return HttpResponse('''<script>alert("Wrong Password!");window.location='/myapp/change_password/'</script>''')

    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')



def edit_student(request,id):
    if request.session["log"] == "lin":
        sobj=Student.objects.get(id=id)
        request.session['stid']=id
        return render(request,"Editstdnt.html",{'data':sobj})
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')


def edit_student_post(request):
    if request.session["log"] == "lin":
        Name=request.POST['textfield']
        Place=request.POST['textfield2']
        PostOffice = request.POST['textfield3']
        Pincode = request.POST['textfield4']
        District = request.POST['textfield5']
        Email = request.POST['textfield6']
        PhoneNumber = request.POST['textfield7']
        ParentName = request.POST['textfield8']
        Parentphonenumber = request.POST['textfield9']
        Department = request.POST['textfield10']
        AdmissionYear = request.POST['textfield11']




        if 'fileField' in request.FILES:

            Photo = request.FILES['fileField']
            fs = FileSystemStorage()
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs.save(date, Photo)
            path = fs.url(date)

            sobj = Student.objects.get(id=request.session['stid'])
            sobj.Name = Name
            sobj.Place = Place
            sobj.Post = PostOffice
            sobj.Pin = Pincode
            sobj.District = District
            sobj.Email = Email
            sobj.Phone = PhoneNumber
            sobj.Parentname = ParentName
            sobj.Parentphonenumber = Parentphonenumber
            sobj.Department = Department
            sobj.AdmissionYear = AdmissionYear
            sobj.Photo = path
            sobj.save()
            return HttpResponse("ok")
        else:
            sobj = Student.objects.get(id=request.session['stid'])
            sobj.Name = Name
            sobj.Place = Place
            sobj.Post = PostOffice
            sobj.Pin = Pincode
            sobj.District = District
            sobj.Email = Email
            sobj.Phone = PhoneNumber
            sobj.Parentname = ParentName
            sobj.Parentphonenumber = Parentphonenumber
            sobj.Department = Department
            sobj.AdmissionYear = AdmissionYear
            sobj.save()

            return HttpResponse('''<script>alert("Update Successfull");window.location='/myapp/view_details/'</script>''')
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')


def view_attendance(request):
    if request.session["log"] == "lin":
        vattnd=Attendance.objects.all()
        return render(request,"viewattndnc.html",{"data":vattnd})
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')



def view_attendance_post(request):
    if request.session["log"] == "lin":
        Search = request.POST['form1']
        return HttpResponse("ok")
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')


def view_details(request):
    if request.session["log"] == "lin":
        vstd=Student.objects.all()
        return render(request,"viewdetails.html",{"data":vstd})
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')



def view_details_post(request):
    if request.session["log"] == "lin":
        From = request.POST['frm']
        To = request.POST['to']
        return HttpResponse("ok")
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')

def delete_student(request,id):
    if request.session["log"] == "lin":
        dstd=Student.objects.filter(id=id).delete()
        return HttpResponse('''<script>alert("Delete Successfull");window.location='/myapp/view_details/'</script>''')
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')


def home(request):
    if request.session["log"] == "lin":
        return render(request,"home.html")
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')
def search(request):
    if request.session["log"] == "lin":
        name=request.POST['search']
        vstd=Student.objects.filter(Name__contains=name)
        return render(request,"viewdetails.html",{'data':vstd})
    else:
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')

def logout(request):
        request.session["log"]=""
        return HttpResponse('''<script>alert("You are already logged out ");window.location='/myapp/login/'</script>''')
