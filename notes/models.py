from django.db import models

class Tags(models.Model):
    tag = models.TextField()
    def __str__(self):
        return f"{self.id}. {self.tag}"
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"
    
class Fact(models.Model):
    descricao = models.TextField()
    curtidas = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.descricao}. {self.curtidas}"
    