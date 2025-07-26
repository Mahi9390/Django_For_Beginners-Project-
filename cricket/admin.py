from django.contrib import admin

# Register your models here.

from .models import players

class MemberAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","phone","joined_date",)
# Register your models here.
admin.site.register(players,MemberAdmin)