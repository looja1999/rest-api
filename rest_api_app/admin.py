from django.contrib import admin
from rest_api_app.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = [ 'username', 'first_name', 'last_name', 'email', 'birth_date' ]
    list_display = fields
    search_fields = fields
