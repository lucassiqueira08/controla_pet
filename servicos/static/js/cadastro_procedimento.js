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

// Cadastro de Diagnóstico
$('#buscarAnimalDiagnostico').on('click', function (e) {
  if ($('#selectAnimalDiagnostico').val().trim() != '') {
    e.preventDefault()
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
            type: "GET",
            url: '/servicos/get_animal',
            headers:{
                "X-CSRFToken": csrftoken,
            },
            data:{
              id_animal     : $('#selectAnimalDiagnostico').val(),
              cpf_cliente     : $('#cpf_cliente_diagnostico').val(),
            },
            success: function (data) {
              $('#nomeAnimalDiagnostico').val(data[0].fields.nome)
              $('#racaAnimalDiagnostico').val(data[0].fields.raca)
              $('#donoAnimalDiagnostico').val(data[0].fields.nome)
              $('#url_foto_diagnostico').attr('src', data[0].fields.url_foto)
             },
        })
  }
  else {
    alerta("Por favor selecione um cliente e animal válido..", "aviso", 5000)
    setTimeout(function(){
      $("#btnConfirmacaoPrevDiagnostico").click()
    },1);
  }
})
$('#cpf_cliente_diagnostico').on('blur', function (e) {
  //Limpa valores atuais
  $('#selectAnimalDiagnostico option').remove()
  $('#selectAnimalDiagnostico').append("<option/>")
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
      cpf_cliente     : $('#cpf_cliente_diagnostico').val(),
    },
    success: function (data) {
      var selectAnimais = $('#selectAnimalDiagnostico')
      var animais = data
      for (var animal in animais) {
        var option = $('<option/>').val(animais[animal].pk)
        .text(animais[animal].fields.nome)
        selectAnimais.append(option)
      }
    },
  })
})
$('#btnConfirmacaoNextDiagnostico').on('click', function(e){
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "GET",
          url: '/servicos/get_diagnostico',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{},
          success: function (data) {
            var tipos = data
            var html = ''
            x = 0
            y = 0
            while (x < tipos.length){
                html = html + '<p class="centro-esquerda">'+tipos[x].tipo.nome+'</p> <ul>'
                while (y < tipos[x].diagnosticos.length){
                  html = html + '<li class="centro-esquerda"><input class="formInputCheckbox" type="checkbox" value="True">'+tipos[x].diagnosticos[y].descricao+'</li>'
                  y++
                }
                y = 0
                html = html + '</ul>'
                x++
            }
            $('#conteudoDiagnostico').append(html)
        }

      })
})
// Ajax - POST - pagina cadastro_diagnostico
$('#btnDiagnosticoSalvar').on('click', function (e) {
  var file;
  $('#file_input_diagnostico').on('change', function(){
    file = event.target.files;
  });
  e.preventDefault()
  var data = new FormData($('#formCadastroDiagnostico').get(0));
  data.append('file', $('#file_input_diagnostico')[0].files);
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/servicos/cadastrar_diagnostico',
          headers:{"X-CSRFToken": csrftoken},
          data:data,
          processData: false,
          contentType: false,
          dataType: "json",
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.dic_animal.tipo=='ok') {
              $('#cpf_cliente_diagnostico').val('')
              let timerId = setInterval(() => window.location.reload(), data.time);
            }
          },
      })
})
