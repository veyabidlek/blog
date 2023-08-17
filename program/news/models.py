from django.db import models

# Create your models here.
class Articles(models.Model):
  title = models.CharField('Title', max_length=50)
  anons = models.CharField('Description', max_length=250)
  fullText = models.TextField('Text')
  date = models.DateTimeField('Publication Date')
  
  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "Article"
    verbose_name_plural = "Articles"
  