from django.forms import ModelForm
from .models import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'valor', 'descricao', 'observacoes', 'categoria']

    def __init__(self, *args, **kwargs):
        super(TransacaoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'