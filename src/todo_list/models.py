from django.db import models

# Create your models here.

class List(models.Model):
    item= models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    completed = models.BooleanField(default = False)

    

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"

    def __str__(self):
        return self.item