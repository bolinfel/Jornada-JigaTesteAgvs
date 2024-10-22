import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JigaTesteAGVS.settings')
django.setup()

from testes.models import tbPropriedades, tbPlacas, tbTipos
'''
    FK_PLACA = models.ForeignKey(tbPlacas, on_delete=models.CASCADE)
    FK_TIPO = models.ForeignKey(tbTipos, on_delete=models.CASCADE)
    PORTA = models.IntegerField()
    DESCRICAO = models.CharField(max_length=20)
'''
import pandas as pd
df = pd.read_csv(r"/home/bolinfel/Documents/draft dBase - tbPropriedades.csv",sep=',')

for (rowName, rowData) in df.iterrows():
    if rowData.ID > 6:
        tipo = tbTipos.objects.get(COD=rowData.FK_TIPO[-4:])
        placa = tbPlacas.objects.all()[0]
        print(rowData.DESCRICAO)
        tbPropriedades.objects.create(FK_PLACA=placa,FK_TIPO=tipo,PORTA=rowData.PORTA,DESCRICAO=rowData.DESCRICAO)