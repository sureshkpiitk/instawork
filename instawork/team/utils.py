import re

from django.core.exceptions import ValidationError


def mobile_validator(value):
    regex = r'^(?:\+?91)?[6789]\d{9}$'
    rule = re.compile(regex)
    if not rule.search(value):
        msg = "Invalid mobile number."
        raise ValidationError(msg)
