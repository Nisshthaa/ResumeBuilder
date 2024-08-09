from django.db import models
from django.contrib.auth.models import User

PERFORMANCE_TYPE_CHOICES = [
    ('percentage', 'Percentage'),
    ('cgpa', 'CGPA '),
    
]

BOARD_CHOICES = [
    ('cbse', 'Central Board of Secondary Education (CBSE)'),
    ('icse', 'Council for the Indian School Certificate Examinations (CISCE/ICSE)'),
    ('nios', 'National Institute of Open Schooling (NIOS)'),
    ('ib', 'International Baccalaureate (IB)'),
    ('cambridge', 'Cambridge International Examinations (CIE)'),
    ('state-board', 'State Boards'),
    ('up-board', 'Uttar Pradesh Board of High School and Intermediate Education'),
    ('maharashtra-board', 'Maharashtra State Board of Secondary and Higher Secondary Education'),
    ('tamilnadu-board', 'Tamil Nadu State Board'),
    ('westbengal-board', 'West Bengal Board of Secondary Education'),
    ('karnataka-board', 'Karnataka Secondary Education Examination Board'),
    ('andhra-board', 'Andhra Pradesh Board of Secondary Education'),
    ('gujarat-board', 'Gujarat Secondary and Higher Secondary Education Board'),
    ('kerala-board', 'Kerala Board of Higher Secondary Education'),
    ('rajasthan-board', 'Board of Secondary Education Rajasthan'),
    ('punjab-board', 'Punjab School Education Board'),
    ('haryana-board', 'Board of School Education Haryana'),
    ('madhya-pradesh-board', 'Madhya Pradesh Board of Secondary Education'),
    ('bihar-board', 'Bihar School Examination Board'),
    ('chhattisgarh-board', 'Chhattisgarh Board of Secondary Education'),
    ('jharkhand-board', 'Jharkhand Academic Council'),
    ('assam-board', 'Board of Secondary Education Assam'),
    ('odisha-board', 'Board of Secondary Education Odisha'),
]
class personalinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    about=models.TextField(default='tell about yourself')

class graduation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college=models.CharField(max_length=300)
    start_year=models.IntegerField()
    end_year=models.IntegerField()
    degree=models.CharField(max_length=300)
    stream=models.CharField(max_length=200)
    performance_type = models.CharField(max_length=50, choices=PERFORMANCE_TYPE_CHOICES)
    score=models.DecimalField(max_digits=10, decimal_places=2)


class SeniorSecondary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school=models.CharField(max_length=300)
    start_year=models.IntegerField()
    end_year=models.IntegerField()
    board= models.CharField(max_length=255, choices=BOARD_CHOICES, blank=True)
    stream=models.CharField(max_length=200)
    performance_type = models.CharField(max_length=50, choices=PERFORMANCE_TYPE_CHOICES)
    score=models.DecimalField(max_digits=10, decimal_places=2)
    


class Secondary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school=models.CharField(max_length=300)
    start_year=models.IntegerField()
    end_year=models.IntegerField()
    board= models.CharField(max_length=255, choices=BOARD_CHOICES, blank=True)
    performance_type = models.CharField(max_length=50, choices=PERFORMANCE_TYPE_CHOICES)
    score=models.DecimalField(max_digits=10, decimal_places=2)
    


class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation=models.CharField(max_length=220)
    profile=models.CharField(max_length=200)
    organisation=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    description=models.TextField()

class internship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation=models.CharField(max_length=220)
    profile=models.CharField(max_length=200)
    organisation=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    description=models.TextField()

class skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill=models.CharField(max_length=100)

class projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    description=models.TextField()

class certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_program=models.CharField(max_length=300)
    organisation=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)

class portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)




