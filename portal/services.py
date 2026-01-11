from django.db import transaction
from .models import Application

@transaction.atomic
def apply_for_job(job, user):
    Application.objects.get_or_create(
        job=job,
        applicant=user
    )
