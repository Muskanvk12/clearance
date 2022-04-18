from django.contrib import admin
from .models import Studentinfo
# Register your models here.

@admin.register(Studentinfo)
class StudentInfoAdmin(admin.ModelAdmin):
	# pass
	list_display = ['student','id','student','roll','branch','sem','year','status']
# admin.site.register(Studentinfo)
