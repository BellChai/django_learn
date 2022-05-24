from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("分类", max_length=100)

    def __str (self):
        return '<Category>[{}]'.format(self.name)
    
    class Meta:
        db_table = 'category'
        ordering = ['-id']
