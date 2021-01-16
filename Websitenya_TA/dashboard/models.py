from django.db import models

# Create your models here.
class Data_sensor(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    curah_hujan = models.FloatField(max_length=30)
    # suhu = models.FloatField(max_length=30)
    # intensitas_cahaya = models.FloatField(max_length=30)
    # ph = models.FloatField(max_length=30)
    # salinitas = models.FloatField(max_length=30)
    # ketinggian_air = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.tanggal)


class Daftar_sensor(models.Model):
    nama = models.CharField(max_length=30)
    deskripsi = models.TextField(max_length=5000)

    def __str__(self):
        return self.nama

class Data_permenit(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    curah_hujan = models.FloatField(max_length=30)
    # suhu = models.FloatField(max_length=30)
    # intensitas_cahaya = models.FloatField(max_length=30)
    # ph = models.FloatField(max_length=30)
    # salinitas = models.FloatField(max_length=30)
    # ketinggian_air = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.tanggal)


class Data_perjam(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    curah_hujan = models.FloatField(max_length=30)
    # suhu = models.FloatField(max_length=30)
    # intensitas_cahaya = models.FloatField(max_length=30)
    # ph = models.FloatField(max_length=30)
    # salinitas = models.FloatField(max_length=30)
    # ketinggian_air = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.tanggal)


class Data_perhari(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    curah_hujan = models.FloatField(max_length=30)
    # suhu = models.FloatField(max_length=30)
    # intensitas_cahaya = models.FloatField(max_length=30)
    # ph = models.FloatField(max_length=30)
    # salinitas = models.FloatField(max_length=30)
    # ketinggian_air = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.tanggal)
