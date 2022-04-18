from django.contrib import admin
from .models import Staffinfo
from .models import Designpattern
from .models import Artificialintelligence
from .models import Computernetwork
from .models import Sepm
from .models import Functionalenglish
from .models import Accountsection
from .models import Hod
from .models import Accountsection
from .models import Library
from .models import Scholarship
from .models import Sports
from .models import Ncc
from .models import Nss
from .models import Final

# Register your models here.


@admin.register(Staffinfo)
class StaffInfoAdmin(admin.ModelAdmin):
    list_display = ['staff', 'id', 'staff', 'dept', 'subject']


l = ['stud', 'id', 'name', 'roll', 'year', 'dept', 'sem', 'status']


@admin.register(Designpattern)
class DPAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Artificialintelligence)
class AIAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Computernetwork)
class CNAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Sepm)
class SempAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Functionalenglish)
class FEAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Hod)
class HODAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Library)
class LibAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Accountsection)
class AccAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Scholarship)
class SchAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Ncc)
class NccAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Nss)
class NssAdmin(admin.ModelAdmin):
    list_display = l


@admin.register(Final)
class FinalAdmin(admin.ModelAdmin):
    list_display = ['stud', 'name', 'roll', 'sem', 'year', 'hod', 'sepm',
                    'fe', 'dp', 'ai', 'cn', 'acc', 'lib', 'scholar', 'ncc', 'nss', 'sports']
