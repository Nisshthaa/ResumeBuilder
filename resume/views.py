from django.shortcuts import render,redirect
from resume.forms import *
from django.contrib.auth.decorators import login_required
from resume.forms import SkillFormSet
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views import View
from resume.models import *



def register (request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST. get('email')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'Username already exists')
            return redirect('login')
        
        user=User.objects.create(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()
        messages.info(request,'Account created Successfully')
        return redirect('login')
    return render(request,'register.html')
    


def login_page(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('personalinfo')


    return render(request,'login.html')

def home_page(request):
    return render(request,'home.html')
  

def base(request):
    return render(request,'base.html')

@login_required
def personal_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        form=PersonalinfoForm(request.POST)

        if form.is_valid():
            personal=form.save(commit=False)
            personal.user=request.user
            personal.save()
            
            return redirect('graduation')

    else:
        form=PersonalinfoForm()  
    return render(request,'personal.html',{'form':form})

@login_required
def graduation_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        form=GraduationForm(request.POST)

        if form.is_valid():
            graduation=form.save(commit=False)
            graduation.user=request.user
            graduation.save()
            
            return redirect('seniorsecondary')

    else:
        form=GraduationForm()  
    return render(request,'graduation.html',{'form':form})

@login_required 
def seniorsecondary_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        form=SeniorSecondaryForm(request.POST)

        if form.is_valid():
            seniorsecondary=form.save(commit=False)
            seniorsecondary.user=request.user
            seniorsecondary.save()
            
            return redirect('secondary')

    else:
        form=SeniorSecondaryForm()  
    return render(request,'seniorsecondary.html',{'form':form})

@login_required  
def secondary_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        form=SecondaryForm(request.POST)

        if form.is_valid():
            secondary=form.save(commit=False)
            secondary.user=request.user
            secondary.save()
            
            return redirect('jobs')

    else:
        form=SecondaryForm()  
    return render(request,'secondary.html',{'form':form})
@login_required
def jobs_info(request):
    if request.method == 'POST':
        formset = JobFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('internships') 
    else:
        formset = JobFormSet(queryset=Jobs.objects.none())
    return render(request, 'jobs.html', {'formset': formset})
@login_required
def internships_info(request):
    if request.method == 'POST':
        formset = InternshipFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('skills') 
    else:
        formset = InternshipFormSet(queryset=internship.objects.none())
    return render(request, 'internships.html', {'formset': formset})
@login_required
def skills_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        formset = SkillFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    skill = form.save(commit=False)
                    skill.user = request.user
                    skill.save()
            return redirect('projects')  # Redirect to the next step
    else:
        formset = SkillFormSet(queryset=skills.objects.none())
    return render(request, 'skills.html', {'formset': formset})
@login_required
def projects_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        formset = ProjectFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    project= form.save(commit=False)
                    project.user = request.user
                    project.save()
            return redirect('certifications')  # Redirect to the next step
    else:
        formset = ProjectFormSet(queryset=projects.objects.none())
    return render(request, 'projects.html', {'formset': formset})
@login_required
def certifications_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        formset = certificationFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    certification = form.save(commit=False)
                    certification.user = request.user
                    certification.save()
            
            return redirect('urls') 
    else:
        formset = certificationFormSet(queryset=projects.objects.none())
    return render(request, 'certifications.html', {'formset': formset})

@login_required

def urls_info(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        formset = PortfolioFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    url = form.save(commit=False)
                    url.user = request.user
                    url.save()
            
            return redirect('resume_template') 
    else:
        formset = PortfolioFormSet(queryset=portfolio.objects.none())
    return render(request, 'urls.html', {'formset': formset})

class resume_template(View):
    def get(self,request):
         
        
        user=request.user
        personal_detail=personalinfo.objects.filter(user=user).first()
        graduation_detail=graduation.objects.filter(user=user).first()
        seniorsecondary_detail=SeniorSecondary.objects.filter(user=user).first()
        secondary_detail=Secondary.objects.filter(user=user).first()
        job_detail=Jobs.objects.filter(user=user)
        internship_detail=internship.objects.filter(user=user)
        skill_detail=skills.objects.filter(user=user)
        project_detail=projects.objects.filter(user=user)
        certification_detail=certification.objects.filter(user=user)
        url_detail=portfolio.objects.filter(user=user).first()
        
        cgpa_types = ['CGPA']
        
        return render(request,'resume_template.html',{'personal_detail':personal_detail,'graduation_detail':graduation_detail,'seniorsecondary_detail':seniorsecondary_detail,'secondary_detail':secondary_detail,'cgpa_types':cgpa_types,'internship_detail':internship_detail,'job_detail':job_detail,'skill_detail':skill_detail,'project_detail': project_detail,'certification_detail':certification_detail,'url_detail':url_detail})
    

   