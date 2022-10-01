from django.contrib import admin
from libapp.models import WORK,Book_Issue

# Register your models here.
#admin.site.register(WORK)
#admin.site.register(Book_Issue)

# Register Work table using method 1:

@admin.register(WORK)

class WORK(admin.ModelAdmin):

   
    list_display=['id','bookname','author','publication','date']
    list_filter=['publication','author']
    
    



# Register book issue table using method 2:

class Book_IssueAdmin(admin.ModelAdmin):


    list_display=['id','studentname','bookname','issuedate','returndate','charge']
    list_filter=['bookname']


admin.site.register(Book_Issue,Book_IssueAdmin)




