from django.db import models
from mapel.models import mapel

jenisKelamin=(
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan','Perempuan'),
    ('Lainnya', 'Lainnya')
)
agama =(
    ('Islam', 'Islam'),
    ('Kristen', 'Kristen'),
    ('Katolik', 'Katolik'),
    ('Budha', 'Budha'),
    ('Hindu', 'Hindu'),
    ('Konghucu', 'Konghucu'),
    ('Lainnya', 'Lainnya')
)
class guru(models.Model):
    class Meta:
        db_table = 'gurus'

    id = models.AutoField(primary_key=True)
    nip = models.IntegerField(default=0,unique=True)
    fullName = models.CharField(max_length=255,unique=True)
    username = models.CharField(max_length=100,unique=True)
    alamat = models.TextField()
    tempatLahir = models.CharField(max_length=255)
    tanggalLahir = models.IntegerField(default=0)
    Agama = models.CharField(max_length=255,choices=agama)
    jenisKelamin = models.CharField(max_length=255,choices=jenisKelamin)
    email = models.EmailField(max_length=255)
    noTelepon = models.IntegerField(default=0)
    mapel1 = models.ForeignKey(mapel,on_delete=models.CASCADE,related_name='mapel1')
    mapel2 = models.ForeignKey(mapel,on_delete=models.CASCADE,null=True,blank=True,default='',related_name='mapel2')
    mapel3 = models.ForeignKey(mapel,on_delete=models.CASCADE,null=True,blank=True,default='',related_name='mapel3')
    mapel4 = models.ForeignKey(mapel,on_delete=models.CASCADE,null=True,blank=True,default='',related_name='mapel4')
    mapel5 = models.ForeignKey(mapel,on_delete=models.CASCADE,null=True,blank=True,default='',related_name='mapel5')
    image = models.FileField('Image',null=True,blank=True)

    def __str__(self):
        self.fullName
