from django.db import models


jurusan =(
    ('TKJ', 'TKJ'),
    ('MM', 'MM'),
    ('PDR', 'PDR'),
    ('OTKP', 'OTKP'),
    ('AKL', 'AKL'),
    ('PM', 'PM'),
    ('PS','PS'),
)
kelas =(
    ('X', 'X'),
    ('XI','XI'),
    ('XII', 'XII')
)
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


class siswa(models.Model):
    class Meta:
        db_table = 'siswas'

    id = models.AutoField(primary_key=True)
    nis = models.IntegerField(default=0, unique=True)
    fullName = models.CharField(max_length=100, unique=True)
    alamat = models.TextField(max_length=500)
    jurusan = models.CharField("Jurusan",max_length=255,choices=jurusan)
    tempatLahir = models.CharField(max_length=255)
    tanggalLahir = models.IntegerField(default=0)
    Agama = models.CharField(max_length=255,choices=agama)
    jenisKelamin = models.CharField(max_length=255,choices=jenisKelamin)
    kelas = models.CharField(max_length=255, choices=kelas)
    noTelepon = models.IntegerField(default=0)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.FileField("Image",null=True, blank=True)



    def __str__(self):
        return self.full_name
