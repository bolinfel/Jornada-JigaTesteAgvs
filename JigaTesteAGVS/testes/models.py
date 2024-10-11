from django.db import models

# Create your models here.
class tbPlacas(models.Model):
    NOME = models.CharField(max_length=30)
    COD = models.CharField(max_length=4)
    ADD_CAN = models.CharField(max_length=30)

class tbTipos(models.Model):
    NOME = models.CharField(max_length=30)
    COD = models.CharField(max_length=4)

class tbPropriedades(models.Model):
    FK_PLACA = models.ForeignKey(tbPlacas, on_delete=models.CASCADE)
    FK_TIPO = models.ForeignKey(tbTipos, on_delete=models.CASCADE)
    PORTA = models.IntegerField()
    DESCRICAO = models.CharField(max_length=20)

class tbTestes(models.Model):
    DATA = models.TimeField(verbose_name="TIMESTAMP")
    FK_PLACA = models.ForeignKey(tbPlacas, on_delete=models.CASCADE)
