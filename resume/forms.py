from django import forms
from .models import personalinfo,graduation,SeniorSecondary,Secondary,PERFORMANCE_TYPE_CHOICES, BOARD_CHOICES,Jobs,internship,skills,projects,certification,portfolio
from django.forms import modelformset_factory
class PersonalinfoForm(forms.ModelForm):
    class Meta:
        model=personalinfo
        fields=['name','email','phoneno','city','state','about']


    
class GraduationForm(forms.ModelForm):
    performance_type = forms.ChoiceField(choices=PERFORMANCE_TYPE_CHOICES)
    class Meta:
        model=graduation
        fields=['college', 'start_year', 'end_year', 'degree', 'stream', 
            'performance_type', 'score']
        
        

class SeniorSecondaryForm(forms.ModelForm):
    performance_type = forms.ChoiceField(choices=PERFORMANCE_TYPE_CHOICES)   
    board = forms.ChoiceField(choices=BOARD_CHOICES, required=False)
    
    class Meta:
        model=SeniorSecondary
        fields=[ 'school','start_year', 'end_year','board', 'stream','performance_type', 'score'
             ]
        

class SecondaryForm(forms.ModelForm):
    performance_type = forms.ChoiceField(choices=PERFORMANCE_TYPE_CHOICES)   
    board = forms.ChoiceField(choices=BOARD_CHOICES, required=False)
    
    class Meta:
        model=Secondary
        fields=[ 'school','start_year', 'end_year','board', 'performance_type', 'score'
             ]
       
        
        
class JobsForm(forms.ModelForm):

    location = forms.CharField(required=False)
    profile = forms.CharField(required=False)
    
    
    class Meta:
        model=Jobs
        fields=[ 'designation','profile', 'organisation','location', 'start_date', 'end_date','description'
             ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
        
JobFormSet = modelformset_factory(Jobs, form=JobsForm, extra=1)

class InternshipForm(forms.ModelForm):
    location = forms.CharField(required=False)
    profile = forms.CharField(required=False)
   
    class Meta:
        model = internship
        fields = ['designation', 'profile', 'organisation', 'location', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
InternshipFormSet = modelformset_factory(internship, form=InternshipForm, extra=1)
        
class skillForm(forms.ModelForm):
    class Meta:
        model=skills
        fields=[ 'skill'
             ]
SkillFormSet = modelformset_factory(skills, form=skillForm, extra=1)

class projectForm(forms.ModelForm):
    
    class Meta:
        model=projects
        fields=[ 'title','start_date', 'end_date','description'
             ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
ProjectFormSet = modelformset_factory(projects, form=projectForm, extra=1)
      
class certificationForm(forms.ModelForm):
    
    class Meta:
        model=certification
        fields=[ 'training_program','organisation','start_date', 'end_date'
             ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
certificationFormSet = modelformset_factory(certification, form=certificationForm, extra=1)

class portfolioForm(forms.ModelForm):
    class Meta:
        model=portfolio
        fields=[ 'linkedin','github','portfolio'
             ]
        widgets = {
            'linkedin': forms.URLInput(attrs={'required': False}),
            'github': forms.URLInput(attrs={'required': False}),
            'portfolio': forms.URLInput(attrs={'required': False}),
        }
        
PortfolioFormSet = modelformset_factory(portfolio, form=portfolioForm, extra=1)