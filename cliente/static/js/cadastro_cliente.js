$.getJSON('/cliente/get_cliente', function (data) {
    var selectCliente = $('#tipoCliente')
    var clientes = data
    console.log(selectCliente)
    for (var cliente in clientes) {
        var option = $('<option/>').val(clientes[cliente].pk)
            .text(clientes[cliente].fields.nome)
        selectCliente.append(option)
    }
})
$('#formcadastrocliente').on('submit', function (e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/cliente/cadastrar_cliente',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            nome_cliente: $('#nome_cli').val(),
            cpf_cliente: $('#cpf_cli').val(),
            email_cliente: $('#email_cli').val(),
            cep: $('#cep').val(),
            logradouro: $('#logradouro').val(),
            numero: $('#numero').val(),
            cidade: $('#cidade').val(),
            bairro: $('#bairro').val(),
            estado: $('#estado').val(),
            complemento: $('#complemento').val(),
            id_tipo_cliente: $('#tipoCliente').val(),
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('#nome_cli').val('')
              $('#cpf_cli').val('')
              $('#email_cli').val('')
              $('#cep').val('')
              $('#logradouro').val('')
              $('#numero').val('')
              $('#cidade').val('')
              $('#bairro').val('')
              $('#estado').val('')
              $('#complemento').val('')
              $('#tipoCliente').val('')
            }
          },
      })
})
$('#animal_botao').on('click', function (e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/cliente/cadastrar_animal',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            cpf_cliente: $('#animal_cpf').val(),
            url_foto: $('#animal_url_foto').val(),
            nome: $('#animal_nome').val(),
            especie: $('#animal_especie').val(),
            raca: $('#animal_raca').val(),
            cor: $('#animal_cor').val(),
            datanasc: $('#datanasc').val(),
            sexo: $("input[name='sexo']").val(),
            microchip: $('#animal_microchip').val(),
            status_animal: $("input[name='status_animal']").val(),
            observacao: $('#animal_obs').val(),
            cpf_responsavel: $('#animal_cpf_responsavel').val(),
            nome_responsavel: $('#animal_nome_responsavel').val()
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            alerta(data.dic_responsavel.mensagem, data.dic_responsavel.tipo, data.dic_responsavel.time)
            alerta(data.dic_animal.mensagem, data.dic_animal.tipo, data.dic_animal.time)
            if (data.dic_animal.tipo=='ok') {
              $('#animal_cpf').val('')
              $('#animal_url_foto').val('')
              $('#animal_nome').val('')
              $('#animal_especie').val('')
              $('#animal_raca').val('')
              $('#animal_cor').val('')
              $('#datanasc').val('')
              $("input[name='sexo']").val('')
              $('#animal_microchip').val('')
              $("input[name='status_animal']").val('')
              $('#animal_obs').val('')
              $('#animal_cpf_responsavel').val('')
              $('#animal_nome_responsavel').val('')
              $('#botaoPrev_5').click()
              $('#botaoPrev_4').click()
              $('#botaoPrev_3').click()
              $('#botaoPrev_2').click()
            }
          },
      })
})
