$.getJSON('/cliente/get_cliente', function (data) {
    var selectCliente = $('#tipoCliente')
    var clientes = data
    for (var cliente in clientes) {
        var option = $('<option/>').val(clientes[cliente].pk)
            .text(clientes[cliente].fields.nome)
        selectCliente.append(option)
    }
})

// Ajax - POST -  pagina cadastro_cliente
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

// Ajax - POST - pagina cadastro_animal
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

$('#achar_animal').click(function(){

  cpf_cliente = $('#cpf_cliente').val()
  nome_animal = $('#nome_animal').val()

  $.getJSON('/cliente/get_ficha_animal'+ '/' + cpf_cliente +  '/' + nome_animal , function (data) {
    $('#nome').val(data[0].fields.nome)
    $('#raca').val(data[0].fields.raca)
    $('#dono').val(data[1].fields.nome)
    if (data[0].fields.url_foto == null){
    $('#foto_animal').attr('src','../../static/img/semfoto.jpeg')
      
    }else
    {
    $('#foto_animal').attr('src',data[0].fields.url_foto)
        }
  })

})

$('#voltar').click(function(){

  data=''
  
})

// ------- VISUALIZA CLIENTE ----------- //
// GET - VISUALIZA CLIENTE
function abrirModalCliente(id, nome, cpf, email, cep, logradouro, numero, cidade, bairro, estado, complemento, id_tipo_cliente){
  var cliente = {}
  cliente.id = id
  cliente.nome = nome
  cliente.cpf = cpf
  cliente.email = email
  cliente.cep = cep
  cliente.logradouro = logradouro
  cliente.numero = numero
  cliente.cidade = cidade
  cliente.bairro = bairro
  cliente.estado = estado
  cliente.complemento = complemento
  cliente.id_tipo_cliente = id_tipo_cliente
  $('#modalVisuCliente').modal('show')
  InputModalCliente(cliente)
}
function InputModalCliente(cliente) {
  $("input[name='id']").val(cliente.id)
  $("input[name='nome']").val(cliente.nome)
  $("input[name='cpf']").val(cliente.cpf)
  $("input[name='email']").val(cliente.email)
  $("input[name='cep']").val(cliente.cep)
  $("input[name='logradouro']").val(cliente.logradouro)
  $("input[name='numero']").val(cliente.numero)
  $("input[name='cidade']").val(cliente.cidade)
  $("input[name='bairro']").val(cliente.bairro)
  $("input[name='estado']").val(cliente.estado)
  $("input[name='complemento']").val(cliente.complemento)
  $("input[name='id_tipo_cliente']").val(cliente.id_tipo_cliente)
}
// AJAX - POST E DELETE -PAGINA VISUALIZAR CLIENTE
$('#cli_botao_salvar').on('click', function(e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/cliente/visualizar_cliente',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            id: $("input[name='id']").val(),
            nome: $("input[name='nome']").val(),
            cpf: $("input[name='cpf']").val(),
            email: $("input[name='email']").val(),
            cep: $("input[name='cep']").val(),
            logradouro: $("input[name='logradouro']").val(),
            numero: $("input[name='numero']").val(),
            cidade: $("input[name='cidade']").val(),
            bairro: $("input[name='bairro']").val(),
            estado: $("input[name='estado']").val(),
            complemento: $("input[name='complemento']").val(),
            id_tipo_cliente: $("input[name='id_tipo_cliente']").val(),
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('#cli_botao_fechar').click()
              let timerId = setInterval(() => window.location.reload(), data.time);
            }
          }
      })
})
$('#cli_botao_deletar').on('click', function(e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  id = $("input[name='id']").val()
  $.ajax({
          type: "DELETE",
          url: '/cliente/delete/' + id,
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{},
          success: function (data) {
            if (data.tipo=='ok') {
              $('#cli_botao_fechar').click()
              let timerId = setInterval(() => window.location.reload(), data.time);
            }
            alerta(data.mensagem, data.tipo, data.time)
          }
        })
  })
// ------- VISUALIZA ANIMAL ----------- //
// GET - VISUALIZA ANIMAL
function abrirModal(id, nome, sexo, raca, cor, especie, datanasc, observacao, microchip, cpf_cliente){
  var animal = {}
  animal.id = id
  animal.nome = nome
  animal.sexo = sexo
  animal.raca = raca
  animal.cor = cor
  animal.especie = especie
  animal.datanasc = datanasc
  animal.observacao = observacao
  animal.microchip = microchip
  animal.cpf_cliente = cpf_cliente
  $('#modalVisuAnimal').modal('show')
  InputModalAnimal(animal)
}
function InputModalAnimal(animal) {
  $("input[name='id']").val(animal.id)
  $("input[name='nome']").val(animal.nome)
  $("input[name='sexo']").val(animal.sexo)
  $("input[name='raca']").val(animal.raca)
  $("input[name='cor']").val(animal.cor)
  $("input[name='especie']").val(animal.especie)
  $("input[name='datanasc']").val(animal.datanasc)
  $("input[name='obs']").val(animal.observacao)
  $("input[name='microchip']").val(animal.microchip)
  $("input[name='cpf_cliente']").val(animal.cpf_cliente)
}
// AJAX - POST E DELETE - VISUALIZA ANIMAL
$('#animal_btn_salvar').on('click', function(e) {
  e.preventDefault()
  console.log($("input[name='nome']").val())
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/cliente/visualizar_animal',
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{
            id: $("input[name='id']").val(),
            url_foto: $("input[name='url_foto']").val(),
            nome: $("input[name='nome']").val(),
            sexo: $("input[name='sexo']").val(),
            raca: $("input[name='raca']").val(),
            cor: $("input[name='cor']").val(),
            especie: $("input[name='especie']").val(),
            datanasc: $("input[name='datanasc']").val(),
            obs: $("input[name='obs']").val(),
            microchip: $("input[name='microchip']").val(),
            cpf_cliente: $("input[name='cpf_cliente']").val(),
          },
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('#animal_btn_fechar').click()
              let timerId = setInterval(() => window.location.reload(), data.time);
            }
          }
      })
})
$('#animal_btn_deletar').on('click', function(e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  id = $("input[name='id']").val()
  $.ajax({
          type: "DELETE",
          url: '/cliente/delete/animal/' + id,
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{},
          success: function (data) {
            if (data.tipo=='ok') {
              $('#animal_btn_fechar').click()
            }
            alerta(data.mensagem, data.tipo, data.time)
            let timerId = setInterval(() => window.location.reload(), data.time);
          }
        })
  })


  
$('#achar_animal').on('click', function(e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    cpf_cliente = $('#cpf_cliente').val()
  nome_animal = $('#nome_animal').val()
  $.ajax({
          type: "GET",
          url: '/cliente/get_ficha_animal'+ '/' + cpf_cliente +   '/' + nome_animal,
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{},
          success: function (data) 
          {
            if (data.tipo=='erro') {
              $('#voltar').click()  
              alerta(data.mensagem, data.tipo, data.time)
        
            }
            else{
            $('#nome').val(data[0].fields.nome)
            $('#raca').val(data[0].fields.raca)
            $('#dono').val(data[1].fields.nome)
            $('#sexo').val(data[0].fields.sexo)
            $('#especie').val(data[0].fields.especie)
            $('#microchip').val(data[0].fields.microchip)
            $('#datanasc').val(data[0].fields.datanasc)
            $('#cor').val(data[0].fields.cor)
            $('#bairro').val(data[1].fields.bairro)
            $('#numero').val(data[1].fields.numero)
            $('#cep').val(data[1].fields.cep)
            $('#cidade').val(data[1].fields.cidade)
            $('#estado').val(data[1].fields.estado)
            
            $('#foto_animal').attr('src',data[0].fields.url_foto)

            }

           
          }
        })
  })