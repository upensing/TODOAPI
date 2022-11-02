from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    createdDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
