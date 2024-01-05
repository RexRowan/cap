from django.contrib import admin
from .models import Phonebook

class PhonebookAdmin(admin.ModelAdmin):
    list_display = ("name", "number")


# register model

admin.site.register(Phonebook, PhonebookAdmin)
