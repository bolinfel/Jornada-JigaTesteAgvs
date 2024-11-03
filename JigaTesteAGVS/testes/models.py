from django.db import models

# Create your models here.
class tbPlacas(models.Model):
    NOME = models.CharField(max_length=30)
    COD = models.CharField(max_length=4)
    ADD_CAN = models.CharField(max_length=30)

    def __str__(self):
        return self.NOME

class tbTipos(models.Model):
    NOME = models.CharField(max_length=30)
    COD = models.CharField(max_length=4)

    def __str__(self):
        return self.NOME

class tbPropriedades(models.Model):
    FK_PLACA = models.ForeignKey(tbPlacas, on_delete=models.CASCADE)
    FK_TIPO = models.ForeignKey(tbTipos, on_delete=models.CASCADE)
    PORTA = models.IntegerField()
    DESCRICAO = models.CharField(max_length=20)

    def __str__(self):
        return self.DESCRICAO

class tbTestes(models.Model):
    DATA = models.DateTimeField(verbose_name="TIMESTAMP")
    FK_PLACA = models.ForeignKey(tbPlacas, on_delete=models.CASCADE)
    FK_PROPRIEDADE = models.ForeignKey(tbPropriedades, on_delete=models.CASCADE,blank=True)
    RESULTADO = models.BooleanField()
    TIPO_TESTE = models.CharField(max_length=15)
