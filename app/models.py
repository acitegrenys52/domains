from django.db import models

from app.validators import validate_https


class Domain(models.Model):
    url = models.URLField(validators=[validate_https])

    def __str__(self):
        return self.url
