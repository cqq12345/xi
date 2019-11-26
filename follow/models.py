from django.db import models

# Create your models here.
class follow(model,Model):
    id = model.IntegerField()
    time=model.DateTimeField(auto_now_add=Ture)

