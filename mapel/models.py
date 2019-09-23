from django.db import models

class mapel(models.Model):
    class Meta:
        db_table = 'mapels'

    Jurusan =(
    ('TKJ', 'TKJ'),
    ('MM', 'MM'),
    ('PDR', 'PDR'),
    ('OTKP', 'OTKP'),
    ('AKL', 'AKL'),
    ('PM', 'PM'),
    ('PS','PS'),
    )

    Kelas =(
    ('X','X'),
    ('XI','XI'),
    ('XII','XII'),
    )

    id = models.AutoField(primary_key=True)
    nameMapel = models.CharField(max_length=255,unique=True)
    jurusan = models.CharField(max_length=255,choices=Jurusan)
    kelas = models.CharField(max_length=100,choices=Kelas)

    def __str__(self):
        return self.nameMapel
