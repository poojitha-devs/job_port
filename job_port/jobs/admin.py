from django.contrib import admin
from .models import Job, Application
class JobAdmin(admin.ModelAdmin):
    list_display=('title','role','location','description','salary','company','posted_on')

class ApplicationAdmin(admin.ModelAdmin):
    list_display=('applicant','job','resume_filename')
    
    def resume_filename(self, obj):
        return obj.resume.name if obj.resume else 'No resume'
    resume_filename.short_description = 'Resume File'
admin.site.register(Job,JobAdmin)
admin.site.register(Application,ApplicationAdmin)

# Register your models here.
