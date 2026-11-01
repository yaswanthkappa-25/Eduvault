from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "college_id",
        "branch",
        "year",
        "semester",
        "cgpa",
    )

    search_fields = (
        "full_name",
        "college_id",
        "user__email",
    )

    list_filter = (
        "branch",
        "year",
        "semester",
    )
