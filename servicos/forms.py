from django import forms

from .models import (Orcamento, Atendimento, ProcedimentoEstetico, TipoDiagnostico, TipoExame, TipoProcedimento,
                     ProcedimentoClinico, AtendimentoProcClinico, AtendimentoProcEstetico, Autorizacao, Comissao,
                     DiagnosticoAnimal, Estadia, Exame, FeitoPor, FichaDiagnostico, TipoStatusAtendimento,
                     TipoStatusEstadia, StatusAtendimento, StatusEstadia)


class FormOrcamento(forms.ModelForm):

    class Meta:
        model = Orcamento
        fields = [
            'preco_final',
        ]


class FormAtendimento(forms.ModelForm):

    class Meta:
        model = Atendimento
        fields = [
            'observacao',
            'data_solicitacao',
            'cpf_cliente',
            'id_orcamento',

        ]


class FormProcedimentoEstetico(forms.ModelForm):

    class Meta:
        model = ProcedimentoEstetico
        fields = [
            'nome',
            'descricao',
            'especie',
            'preco',

        ]


class FormTipoDiagnostico(forms.ModelForm):

    class Meta:
        model = TipoDiagnostico
        fields = [
            'nome',
        ]


class FormTipoExame(forms.ModelForm):

    class Meta:
        model = TipoExame
        fields = [
            'nome',
        ]


class FormTipoProcedimento(forms.ModelForm):

    class Meta:
        model = TipoProcedimento
        fields = [
            'nome',
        ]


class FormProcedimentoClinico(forms.ModelForm):

    class Meta:
        model = ProcedimentoClinico
        fields = [
            'nome',
            'descricao',
            'especie',
            'preco',
            'id_tipo_proc',
        ]


class FormAtendimentoProcClinico(forms.ModelForm):

    class Meta:
        model = AtendimentoProcClinico
        fields = [
            'id_atendimento',
            'id_proc_clinico',
        ]


class FormAtendimentoProcEstetico(forms.ModelForm):

    class Meta:
        model = AtendimentoProcEstetico
        fields = [
            'id_atendimento',
            'id_proc_estetico',
        ]


class FormAutorizacao(forms.ModelForm):

    class Meta:
        model = Autorizacao
        fields = [
            'link_doc',
            'id_proc_clinico',
        ]


class FormComissao(forms.ModelForm):

    class Meta:
        model = Comissao
        fields = [
            'valor',
            'id_atendimento',
        ]


class FormDiagnosticoAnimal(forms.ModelForm):

    class Meta:
        model = DiagnosticoAnimal
        fields = [
            'descricao',
            'booleano',
            'id_tipo_diagnostico',
        ]


class FormEstadia(forms.ModelForm):

    class Meta:
        model = Estadia
        fields = [
            'observacao',
            'data_inicio',
            'data_fim',
            'data_solicitacao',
            'valor_diaria',
            'cpf_cliente',
        ]


class FormExame(forms.ModelForm):

    class Meta:
        model = Exame
        fields = [
            'link_doc',
            'nome',
            'data_realizacao',
            'id_animal',
            'id_tipo_exame',
        ]


class FormFeitoPor(forms.ModelForm):

    class Meta:
        model = FeitoPor
        fields = [
            'id_atendimento',
            'id_funcionario',
            'data_realizacao',

        ]


class FormFichaDiagnostico(forms.ModelForm):

    class Meta:
        model = FichaDiagnostico
        fields = [
            'id_diagnostico',
            'id_ficha',
        ]


class FormTipoStatusAtendimento(forms.ModelForm):

    class Meta:
        model = TipoStatusAtendimento
        fields = [
            'nome',
        ]


class FormTipoStatusEstadia(forms.ModelForm):

    class Meta:
        model = TipoStatusEstadia
        fields = [
            'nome_status',
        ]


class FormStatusAtendimento(forms.ModelForm):

    class Meta:
        model = StatusAtendimento
        fields = [
            'id_atendimento',
            'id_status',
        ]


class FormStatusEstadia(forms.ModelForm):

    class Meta:
        model = StatusEstadia
        fields = [
            'id_estadia',
            'id_status',
        ]

