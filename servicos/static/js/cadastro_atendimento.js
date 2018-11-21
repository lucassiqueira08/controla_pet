$('#btnAtendimentoSalvar').on('click', function (e) {
    e.preventDefault()
    var dataProcedimentos = serielizersTable()
    var funcionario = getFuncionario()
    var animal = $('#selectAtendimento').val()
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
          alerta(data.mensagem, data.tipo, data.time)
          if (data.tipo=='ok') {
            let timerId = setInterval(() => window.location.reload(), data.time);
          }
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

$('#cpfAtendimento').on('blur', function (e) {
  //Limpa valores atuais
  $('#selectAtendimento option').remove()
  $('#selectAtendimento').append("<option/>")
   //Busca animais do cliente em específico

  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
    type: "GET",
    url: '/servicos/get_animais_cliente',
    headers:{
      "X-CSRFToken": csrftoken,
    },
    data:{
      cpf_cliente : $('#cpfAtendimento').val(),
    },
    success: function (data) {
      var selectAtendimento = $('#selectAtendimento')
      var animais = data
      for (var animal in animais) {
        var option = $('<option/>').val(animais[animal].pk)
        .text(animais[animal].fields.nome)
        selectAtendimento.append(option)
      }
    },
  })
})

$('#Buscar').on('click', function (e) {
  if ($('#selectAtendimento').val().trim() != '') {
    e.preventDefault()
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
            type: "GET",
            url: '/servicos/get_animal',
            headers:{
                "X-CSRFToken": csrftoken,
            },
            data:{
              id_animal       : $('#selectAtendimento').val(),
              cpf_cliente     : $('#cpfAtendimento').val(),
            },
            success: function (data) {
              var animal = data[0].fields

              $('.nome_animal_table').text(animal.nome)
              $('.cor_animal').text(animal.cor)
              $('.cpf_cliente').text(animal.cpf_cliente)
              $('.sexo_animal').text(animal.sexo)
             },
        })
        $.ajax({
                type: "GET",
                url: '/cliente/get_cliente_id',
                headers:{
                    "X-CSRFToken": csrftoken,
                },
                data:{
                  cpf_cliente     : $('#cpfAtendimento').val(),
                },
                success: function (data) {
                  var cliente = data[0].fields

                  $('.logradouro').text(cliente.logradouro)
                  $('.nome_cliente').text(cliente.nome)
                 },
            })
  }
  else {
    alerta("Por favor selecione um cliente e animal válido..", "aviso", 5000)
    setTimeout(function(){
      $("#btnConfirmacaoPrevAtendimento").click()
    },1);
  }
})
