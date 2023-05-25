from django.db import models

# Create your models here.


class Films(models.Model):

    name = models.TextField('films name')

    def __str__(self) -> str:
        return self.name