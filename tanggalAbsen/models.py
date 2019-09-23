from django.db import models
from absenHarian.models import absenHarian

class absenTanggal(models.Model):
    class Meta:
        db_table = 'absenTanggals'

    id = models.AutoField(primary_key=True)
    tanggal1 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal1')
    tanggal2 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal2')
    tanggal3 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal3')
    tanggal4 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal4')
    tanggal5 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal5')
    tanggal6 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal6')
    tanggal7 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal7')
    tanggal8 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal8')
    tanggal9 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal9')
    tanggal10 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal10')
    tanggal11 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal11')
    tanggal12 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal12')
    tanggal13 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal13')
    tanggal14 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal14')
    tanggal15 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal15')
    tanggal16 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal16')
    tanggal17 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal17')
    tanggal18 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal18')
    tanggal19 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal19')
    tanggal20 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal20')
    tanggal21 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal21')
    tanggal22 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal22')
    tanggal23 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal23')
    tanggal24 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal24')
    tanggal25 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal25')
    tanggal26 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal26')
    tanggal27 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal27')
    tanggal28 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal28')
    tanggal29 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal29')
    tanggal30 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal30')
    tanggal31 = models.ForeignKey(absenHarian,max_length=255, on_delete=models.CASCADE, null=True, blank=True,related_name='tanggal31')

    def __str__(self):
        return self.tanggal1
