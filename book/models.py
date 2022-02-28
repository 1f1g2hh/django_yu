from django.db import models
from acc.models import User
# Create your models here.
class Book(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(User,on_delete =models.CASCADE )
    impo = models.BooleanField()
    pubdate = models.DateTimeField()
    
    def __str__(self):
        return f"[{self.user}]{self.site_name}"
    
    def summary(self):
        if len(self.content) > 13:
            return self.content[:13] + "..."
        return self.content