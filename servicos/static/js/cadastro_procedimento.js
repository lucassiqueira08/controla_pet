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

$('#buscarAnimalEstadia').on('click', function (e) {
  if ($('#selectAnimal').val().trim() != '') {
    e.preventDefault()
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
            type: "GET",
            url: '/servicos/get_animal',
            headers:{
                "X-CSRFToken": csrftoken,
            },
            data:{
              id_animal     : $('#selectAnimal').val(),
              cpf_cliente     : $('#cpf_cliente').val(),
            },
            success: function (data) {
              alert(data)
              $('#nome_animal').val(data.animal[0].fields.nome)
              $('#raca_animal').val(data.animal[0].fields.raca)
              $('#dono_animal').val(data.cliente[0].fields.nome)

            },
        })
  }
  else {
    alerta("Por favor selecione um cliente e animal válido..", "aviso", 5000)
    setTimeout(function(){
      $("#btnConfirmacaoPrev").click()
    },1);
  }
})
$('#cpf_cliente').on('blur', function (e) {
  //Limpa valores atuais
  $('#selectAnimal option').remove()
  $('#selectAnimal').append("<option/>")

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
      cpf_cliente     : $('#cpf_cliente').val(),
    },
    success: function (data) {
      var selectAnimais = $('#selectAnimal')
      var animais = data
      for (var animal in animais) {
        var option = $('<option/>').val(animais[animal].pk)
        .text(animais[animal].fields.nome)
        selectAnimais.append(option)
      }
    },
  })
})
