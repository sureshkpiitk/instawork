import uuid

from django.db import models

# Create your models here.
from team.utils import mobile_validator

ROLES = [
    ("ADMIN", "Admin"),
    ("REGULAR", "Regular")
]


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True, db_index=True)
    mobile = models.CharField(max_length=32, null=True, blank=True, db_index=True, validators=[mobile_validator])
    role = models.CharField(max_length=8, choices=ROLES, default='REGULAR')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)



