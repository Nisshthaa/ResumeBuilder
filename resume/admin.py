from django.contrib import admin
from resume.models import personalinfo,graduation,SeniorSecondary,Secondary,Jobs,internship,skills,portfolio,projects,certification

class personalinfoRegister(admin.ModelAdmin):
    list_display=['name','email','phoneno']
admin.site.register(personalinfo,personalinfoRegister)

class GraduationRegister(admin.ModelAdmin):
    list_display=['college','degree','score']
admin.site.register(graduation,GraduationRegister)

class SeniorSecondaryRegister(admin.ModelAdmin):
    list_display=['school','stream','score']
admin.site.register(SeniorSecondary,SeniorSecondaryRegister)

class SecondaryRegister(admin.ModelAdmin):
    list_display=['school','score']
admin.site.register(Secondary,SecondaryRegister)

class JobsRegister(admin.ModelAdmin):
    list_display=[ 'designation','profile', 'organisation']
admin.site.register(Jobs,JobsRegister)

class internshipRegister(admin.ModelAdmin):
    list_display=[ 'designation','profile', 'organisation']
admin.site.register(internship,internshipRegister)

class skillsRegister(admin.ModelAdmin):
    list_display=[ 'skill']
admin.site.register(skills,skillsRegister)

class portfolioRegister(admin.ModelAdmin):
    list_display=[ 'linkedin','portfolio','github']
admin.site.register(portfolio,portfolioRegister)

class certificationRegister(admin.ModelAdmin):
    list_display=[ 'training_program','organisation']
admin.site.register(certification,certificationRegister)


class projectRegister(admin.ModelAdmin):
    list_display=[ 'title']
admin.site.register(projects,projectRegister)
