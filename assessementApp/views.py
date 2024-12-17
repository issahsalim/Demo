from email import message
from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm,AbsenceReport,LoginForm,FormMasterForms
from .models import Assess_Student,Announcement,FormMaster,Headmaster
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request): 
    return render(request,'home.html')
                         

def index(request):
    return render(request,'index.html')

def register(request):
     if request.method=="POST":
         form=StudentForm(request.POST)
         if form.is_valid():
             new_student=form.save(commit=False)
             indexNumber=form.cleaned_data['username']
             phone=form.cleaned_data['phone']
             stu_email=form.cleaned_data['email']
             parent_Number=form.cleaned_data['parent_number']
             parent_Email=form.cleaned_data['parent_mail']
             password=form.cleaned_data['password']
             c_password=form.cleaned_data['confirm_password']

            #  if not staticIndexNumbers.objects.filter(Student_IndexNumber=indexNumber).exists():
            #     messages.error(request, f"Index {indexNumber} is not in ITB index numbers")
                # return redirect('signup')  
             if len(phone)!=10 or len(parent_Number)!=10: 
                 messages.error(request,'Invalid phone number') 
                 return redirect('signup')
             if phone==parent_Number: 
                 messages.warning(request,"Your number can't be same as your parent own")
                 return redirect('signup')
             if parent_Email==stu_email: 
                 messages.warning(request,"Your email can't be same a your parent own")
                 return redirect('signup')
             if password!=c_password: 
                 messages.error(request,'Password Mismatch')
                 return redirect('signup')
             if len(password)<6: 
                 messages.warning(request,"Weak Password. Password must not be less then 10")
                 return redirect('signup') 
             
             new_student.set_password(form.cleaned_data['password']) 
             new_student.save() 
             messages.success(request,'Account successfully created')
             return redirect('login')
         else: 
             messages.error(request,'Account already exist')
             return redirect('signup') 
     else:  
         form=StudentForm()
         return render(request,'register.html',{'form':form}) 
        

def loginForm(request):
    if request.method=="POST": 
            indexNumber=request.POST.get('index_number')
            password=request.POST.get('password') 
            user=authenticate(request, username=indexNumber,password=password)
            if user is not None: 
                login(request,user)
                return redirect('home') 
            else:     
                messages.error(request,'Invalid index number or password')
                return redirect('login')
            
    return render(request,'login.html') 


def announcement(request):  
     announcement=Announcement.objects.all()
     return render(request,'announcement.html',{'announcement':announcement})    

def absence(request):
    if request.method=="POST": 
        forms= AbsenceReport(request.POST,request.FILES )
        if forms.is_valid():   
                ParentName=forms.cleaned_data['Parent_Name']
                forms.save()  
                messages.success(request,f"Thank you for reporting, {ParentName}")   
                return redirect('absence')  
        
    else:  
        absenceForm=AbsenceReport(initial={'stu_indexNumber': request.user.username})

        return render(request,'absence.html',{'absence_form':absenceForm}) 


def logoutFun(request): 
    logout(request) 
    messages.error(request,'Logout Successfully') 
    return redirect('index') 


# @login_required
# def Assessment(request): 
#     #   if request.user.is_authenticated:  
#          studentIndex=request.user.username 
#          if Assess_Student.objects.filter(index_Number=studentIndex).exists():
#             studentRecord=get_object_or_404(Assess_Student,index_Number=studentIndex) 
#             studentRecord.Total=(studentRecord.Total_Quiz_Marks + studentRecord.Total_Assignment_Mark + studentRecord.Attendance_Mark + studentRecord.Mid_Sem)/3
#             indexNumber=Assess_Student.objects.get(index_Number=studentIndex).index_Number
#             studentRecord.save()   
#             return redirect('Result',index=indexNumber) 
#          else:     
#              messages.error(request,'You have not been assess yet')  
#              return redirect('home') 
#     #   else: 
#     #       return redirect('home')  
# @login_required
# def AssessmentDetail(request,index):  
#    indexNumbers=get_object_or_404(Assess_Student, index_Number=index) 
#    return render(request,'assessment.html',{'studentResult':indexNumbers}) 



def custom_404(request, exception):
    return render(request, '404.html', status=404) 


def addTeach(request):
    # if request.method=="GET":
        searched=request.GET.get('search','') 
        teachers=FormMaster.objects.all() 
        headmaster=Headmaster.objects.all() 
        onpage={'teachers':teachers,'headmaster':headmaster} 
        if searched:
            result=FormMaster.objects.filter(Q(name__icontains=searched) | Q(ClassHanlder__icontains=searched)) 
            if not result:  
                return render(request,'notFound.html',{'errorsearch':searched})  
            return render(request,'formteacher.html',{'search':result})      
            
        return render(request,'formteacher.html',onpage)


 

    