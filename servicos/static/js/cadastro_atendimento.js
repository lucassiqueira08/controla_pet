$('#sendForm').on('submit', function (e) {
    e.preventDefault()
    var dataProcedimentos = serielizersTable()
    var funcionario = getFuncionario()
    var animal = $('.nome_animal_table').data('pk')
    console.log(animal)
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: '/servicos/cadastro_atendimento',
        headers:{
            "X-CSRFToken": csrftoken,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({
            cpf_cliente: $('#cpf').val(),
            nome_animal: animal,
            procedimentos: dataProcedimentos,
            funcionario: funcionario,
            orcamento: $('#precoTotal').text()
        }),
        success: function (data) {

        },
        dataType: 'json',
    })
})

function getFuncionario() {
    var funcionario = $('#escolherFuncionario option:selected').data()
    return funcionario.pk
}

function serielizersTable() {
    var procedimentos = []

    $('#procedimentoSelecionados > tbody').find('tr').each(function(){
        procedimento = {}
        procedimento.pk = $(this).data('pk')
        procedimento.model = $(this).data('model')
        procedimentos.push(procedimento)
    });
    return procedimentos
}

$.getJSON('/usuario/get_funcionario', function (data) {
    var select = $('#escolherFuncionario');
    for (var item in data) {
        var option = $('<option/>').text(
            data[item].fields.primeiro_nome +' '+ data[item].fields.ultimo_nome
        ).data(data[item])
        select.append(option)
    }
})

$.getJSON('/servicos/get_procedimento', function (data) {
    var listaProcedimentoClinico = []
    var listaProcedimentoEstetico = []
    for (var procedimento in data) {
        if (data[procedimento].model == 'servicos.procedimentoclinico') {
            listaProcedimentoClinico.push(data[procedimento])
            continue
        }
        listaProcedimentoEstetico.push(data[procedimento])
    }

    $("#procedimento").change(function () {
        var proc = ($('input[name=procedimento]:checked', '#procedimento').val());
        var selectProc = '';
        var select = $('#escolherProcedimento').html('');

        if (proc == 'clinico') {
            selectProc = listaProcedimentoClinico;
            var autorizacao = $('#clinicoAutorizacao').html('')
            var autorizacao = false;
        } else {
            selectProc = listaProcedimentoEstetico;
            var autorizacao = $('#clinicoAutorizacao').html(
                $('<input/>').attr('placeholder', 'digite o link do documento')
                .addClass('destacadoCimaBaixo').attr('id', 'tt').attr('type', 'text')
                .keyup(valLink)
            )
            var autorizacao = true;
        }

        for (var item in selectProc) {
            if (autorizacao) {
                selectProc[item].autorizacao = valLink
            }

            var option = $('<option/>').text(selectProc[item].fields.nome).data(
                selectProc[item]
            )
            select.append(option)
        }
    })
})

function valLink() {
    var x =  $('#tt').val();
    return x;
}

$('#escolherProcedimento').click(function () {
    var algo = {}
    algo.model = $('#escolherProcedimento option:selected').data('model')
    algo.pk = $('#escolherProcedimento option:selected').data('pk')

    var tdNome = $('<td/>').text($('#escolherProcedimento option:selected').data('fields').nome)
    var tdPreco = $('<td/>').text($('#escolherProcedimento option:selected').data('fields').preco).attr('name', 'preco')
    var tdDescricao = $('<td/>').text($('#escolherProcedimento option:selected').data('fields').descricao)
    var tdLink = $('<td/>').text($('#escolherProcedimento option:selected').data('autorizacao'))
    var tdButton = $('<button/>').prop('type', 'button').click(apagar).text('apagar')
    var tbody = $('#procedimentoSelecionados > tbody')
    var tr = $('<tr/>').data(algo)
    tr.append(tdNome, tdDescricao, tdPreco, tdLink, tdButton)
    tbody.append(tr)

    calculaPreco()
})

function calculaPreco() {
    var soma = 0
    $('#procedimentoSelecionados > tbody > tr').each(function() {
        $(this).find("td[name=preco]").each(function() {
            var cell = $(this).html()
            soma += parseFloat(cell)
        });
    });
    $('#precoTotal').text(soma.toFixed(2))
}

function apagar() {
    $(this).closest("tr").remove()
    calculaPreco()
}

$('#Buscar').click(function () {
    var nomeAnimal = $('#nome_animal').val()
    var nomeCpf = $('#cpf').val()
    $.getJSON('/cliente/get_animal/' + nomeCpf + '/' + nomeAnimal, function (data) {
        var cliente = data[0].fields
        var clienteCpf = data[0].pk
        var animal = data[1].fields

        $('.nome_animal_table').text(animal.nome).data(data[1])
        $('.logradouro').text(cliente.logradouro)
        $('.nome_cliente').text(cliente.nome)
        $('.cor_animal').text(animal.cor)
        $('.cpf_cliente').text(clienteCpf)
        $('.sexo_animal').text(animal.sexo)
    })
})
