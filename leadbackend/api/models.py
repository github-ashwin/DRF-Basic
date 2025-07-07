from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    passout_year = models.CharField(max_length=15)

    SOURCE_OPTION = (
        ("instagram","instagram"),
        ("facebook","facebook"),
        ("referral","referral"),
        ("walkin","walkin")
    )
    source = models.CharField(max_length=100,choices=SOURCE_OPTION,default="walkin")

    COURSE_OPTION = (
        ("TESTING","TESTING"),
        ("PYTHON DJANGO","PYTHON DJANGO"),
        ("MERN","MERN"),
        ("DATA SCIENCE","DATA SCIENCE"),
        ("JAVA SPRINGBOOT","JAVA SPRINGBOOT"),
        (".NET",".NET")
    )
    course = models.CharField(max_length=100,choices=COURSE_OPTION,default="PYTHON DJANGO")

    COURSE_MODE_OPTION = (
        ("ONLINE","ONLINE"),
        ("OFFLINE","OFFLINE"),
        ("HYBRID","HYBRID")
    )
    course_mode = models.CharField(max_length=20,choices=COURSE_MODE_OPTION,default="OFFLINE")

    STATUS_OPTION = (
        ("FOLLOWUP","FOLLOW-UP"),
        ("PROCEEDTOADMISSION","PROCEED-TO-ADMISSION"),
        ("NOTINTERESTED","NOT-INTERESTED")
    )
    status = models.CharField(max_length=20,choices=STATUS_OPTION,default="FOLLOWUP")

    created_date = models.DateTimeField(auto_now_add=True)
    updadted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name