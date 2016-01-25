from django.core.exceptions import ValidationError


def validate_https(value):
    protocol = value[0:5]

    if protocol != "https":
        raise ValidationError('%s is not https' % value)
