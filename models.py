from django.db import models # type: ignore

class Register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    repassword=models.CharField(max_length=40)
    class Meta:
        db_table="game"


# Create your models here.
