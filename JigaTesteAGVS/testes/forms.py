# forms.py
from django import forms
from .models import tbTestes, tbPropriedades

class tbTestesForm(forms.ModelForm):
    num_repeticoes = forms.IntegerField(
        label="Número de Repetições",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite um número'})
    )
    
    class Meta:
        model = tbTestes
        fields = ["FK_PLACA", "FK_PROPRIEDADE"]

    def __init__(self, *args, **kwargs):
        fk_placa = kwargs.pop('fk_placa', None)  # Retrieve fk_placa if provided
        super().__init__(*args, **kwargs)
        
        # Initially empty properties list if no board is selected
        if fk_placa:
            self.fields['FK_PROPRIEDADE'].queryset = tbPropriedades.objects.filter(FK_PLACA=fk_placa)
        else:
            self.fields['FK_PROPRIEDADE'].queryset = tbPropriedades.objects.none()

