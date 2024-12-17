from django.contrib import admin

from .models import staticIndexNumbers,Announcement,absenceReport,Assess_Student,FormMaster,Headmaster


from django.core.cache import cache
from django.contrib import messages



# @admin.register(staticIndexNumbers)
# class  studentIndeNumberAdmin(admin.ModelAdmin):
#      search_fields=("Student_IndexNumber",)  


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display=('title','date',)
    


@admin.register(absenceReport)
class AbsenceReportAdmin(admin.ModelAdmin):  
    list_display=('Student_Name',"Student_Class","Parent_Name",'submitted_date',) 


# @admin.register(Assess_Student)
# class Student_Assess(admin.ModelAdmin):
#     list_display=('index_Number','Total',) 
#     search_fields=('index_Number',)

@admin.register(FormMaster)
class Add_Form_Master(admin.ModelAdmin):
    list_display=('name','phoneNumber',)
    search_fields=("name","phoneNumber","age",)

@admin.register(Headmaster)
class Headmaster(admin.ModelAdmin):
    list_display=("name","phoneNumber") 


admin.site.site_header="ITB Attendance App"




