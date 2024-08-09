from django.contrib import admin
from django.urls import path
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('base/',views.base),
    path('personalinfo/',views.personal_info,name='personalinfo'),
    path('graduation/',views.graduation_info,name='graduation'),
    path('seniorsecondary/',views.seniorsecondary_info,name='seniorsecondary'),
    path('secondary/',views.secondary_info,name='secondary'),
    path('jobs/',views.jobs_info,name='jobs'),
    path('internships/',views.internships_info,name='internships'),
    path('skills/',views.skills_info,name='skills'),
    path('projects/',views.projects_info,name='projects'),
    path('certifications/',views.certifications_info,name='certifications'),
    path('urls/',views.urls_info, name='urls'),
    
    path('resume_template/',views.resume_template.as_view(),name='resume_template'),
 
]