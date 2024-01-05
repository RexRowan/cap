from django.db import models


class Phonebook(models.Model):
    name=models.CharField(max_length=120)
    number=models.CharField(max_length=120)

    def __stir__(self):
        return self.name
