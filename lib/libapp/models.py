
from django.db import models

# Create your models here.

class WORK(models.Model):
    bookname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    publication=models.CharField(max_length=30)
    date=models.DateField()
    uid=models.IntegerField()
    is_deleted=models.CharField(max_length=10)

    def __str__(self):
        return self.bookname


class Book_Issue(models.Model):
    studentname=models.CharField(max_length=50)
    bookname=models.CharField(max_length=50)
    issuedate=models.DateField()
    returndate=models.DateField()
    charge=models.IntegerField()
    is_deleted=models.CharField(max_length=10)



