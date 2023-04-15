from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)
    def __str__(self) -> str:
        return self.topic_name

class WebPages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    url=models.URLField()
    email=models.EmailField()
    def __str__(self) -> str:
        return self.name
class AcessRecord(models.Model):
    name=models.ForeignKey(WebPages,on_delete=models.CASCADE)
    auther=models.CharField(max_length=20)
    date=models.DateField()
    def __str__(self) -> str:
        return self.auther