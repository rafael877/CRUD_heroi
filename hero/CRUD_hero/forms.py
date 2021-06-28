from django import forms
from .models import Heroi

class FormularioHeroi(forms.ModelForm):
  class Meta:
    model = Heroi
    fields = ['nome', 'idade', 'imagem', 'poder', 'descricao']