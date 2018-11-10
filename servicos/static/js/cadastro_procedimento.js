$.getJSON('/servicos/get_tipo_procedimento', function (data) {
    var selectProcedimento = $('#C_tipoProcedimento')
    var procedimentos = data

    for (var procedimento in procedimentos) {
        var option = $('<option/>').val(procedimentos[procedimento].pk)
            .text(procedimentos[procedimento].fields.nome)
        selectProcedimento.append(option)
    }
})

$('#FormCadastroProcedimentoEstetico').on('submit', function (e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/servicos/cadastro_procedimento',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            nome                  : $('#E_nome').val(),
            descricao             : $('#E_descricao').val(),
            preco                 : $('#E_preco').val(),
            especie               : $('#E_especie').val(),
            aba_procedimento      : 'estetico',
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('.formEtapasInput').val('')
              $('.formInput').val('')
            }
          },
      })
})

$('#FormCadastroProcedimentoClinico').on('submit', function (e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/servicos/cadastro_procedimento',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            nome                  : $('#C_nome').val(),
            descricao             : $('#C_descricao').val(),
            preco                 : $('#C_preco').val(),
            especie               : $('#C_especie').val(),
            tipo_procedimento     : $('#C_tipoProcedimento').val(),
            aba_procedimento      : 'clinico',
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('.formEtapasInput').val('')
              $('.formInput').val('')
            }
          },
      })
})

//====================CADASTRO DE ESTADIA====================

$('#cpfCliente').on('blur', function (e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/servicos/cadastro_estadia',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            nome                  : $('#nome').val(),
            raca                  : $('#raca').val(),
            dono                  : $('#dono').val(),
            especie               : $('#C_especie').val(),
            tipo_procedimento     : $('#C_tipoProcedimento').val(),
            aba_procedimento      : 'clinico',
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('.formEtapasInput').val('')
              $('.formInput').val('')
            }
          },
      })
  $.getJSON('/cliente/get_animais_cliente/', function (data) {
      var selectCliente = $('#tipoCliente')
      var clientes = data
      for (var cliente in clientes) {
          var option = $('<option/>').val(clientes[cliente].pk)
              .text(clientes[cliente].fields.nome)
          selectCliente.append(option)
      }
  })
})

$('#buscarAnimalEstadia').on('click', function (e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/servicos/cadastro_estadia',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            nome                  : $('#nome').val(),
            raca                  : $('#raca').val(),
            dono                  : $('#dono').val(),
            especie               : $('#C_especie').val(),
            tipo_procedimento     : $('#C_tipoProcedimento').val(),
            aba_procedimento      : 'clinico',
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('.formEtapasInput').val('')
              $('.formInput').val('')
            }
          },
      })
})
