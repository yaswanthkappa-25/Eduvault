from django.db import models
from django.conf import settings


class StudentProfile(models.Model):

    YEAR_CHOICES = [
        ("1", "1st Year"),
        ("2", "2nd Year"),
        ("3", "3rd Year"),
        ("4", "4th Year"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    full_name = models.CharField(max_length=100)

    college_id = models.CharField(
        max_length=30,
        unique=True
    )

    branch = models.CharField(max_length=100)

    year = models.CharField(
        max_length=1,
        choices=YEAR_CHOICES,
        default="4"
    )

    semester = models.PositiveSmallIntegerField(
        default=1
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )

    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name