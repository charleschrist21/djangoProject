from django.db import models

# Create your models here.
class admin(models.Model):
    class Meta:
        db_table = 'admin'

    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    image = models.FileField('Image',null=True,blank=True)

    def __str__(self):
        return self.fullName
