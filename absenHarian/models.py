from django.db import models

izin=(
    ('Masuk','Masuk'),
    ('Izin','Izin'),
    ('Sakit','Sakit'),
    ('Alpa','Alpa')
)

class absenHarian(models.Model):
    class Meta:
        db_table = 'absenHarian'

    id = models.AutoField(primary_key=True)
    jam1 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam2 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam3 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam4 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam5 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam6 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam7 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam8 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam9 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam10 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam11 = models.CharField(max_length=255,null=True,blank=True,choices=izin)
    jam12 = models.CharField(max_length=255,null=True,blank=True,choices=izin)

    def __str__(self):
        return self.jam1
