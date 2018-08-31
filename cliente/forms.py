from django import forms

from .models import Cliente, Animal, FichaAnimal, Responde, Responsavel, TipoStatusAnimal, StatusAnimal


class FormCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'cpf',
            'nome',
            'email',
            'logradouro',
            'bairro',
            'cidade',
            'cep',
            'numero',
            'complemento',
            'id_tipo_cliente',
        ]


class FormAnimal(forms.ModelForm):

    class Meta:
        model = Animal
        fields = [
            'nome',
            'sexo',
            'especie',
            'raca',
            'cor',
            'datanasc',
            'observacao',
            'microchip',
            'cpf_cliente',
        ]


class FormFichaAnimal(forms.ModelForm):

    class Meta:
        model = FichaAnimal
        fields = [
            'data_consulta',
            'descricao',
        ]


class FormResponde(forms.ModelForm):

    class Meta(forms.ModelForm):
        Model = Responde
        fields = [
            'cpf_responsavel',
            'id_animal',
        ]


class FormResponsavel(forms.ModelForm):

    class Meta(forms.ModelForm):
        Model = Responsavel
        fields = [
            'cpf',
            'nome',
        ]


class FormTipoStatusAnimal(forms.ModelForm):

    class Meta(forms.ModelForm):
        Model = TipoStatusAnimal
        fields = [
            'nome'
        ]

class FormStatusAnimal(forms.ModelForm):

    class Meta(forms.ModelForm):
        Model = StatusAnimal
        fields = [
            'id_status',
            'id_animal'
        ]