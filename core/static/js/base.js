$.get('/get_notificacao', function(data){

  var dataJson = JSON.parse(data)

  var notificacao = $('#notificacoes')
  for (var item in dataJson) {
    var id = $('<p/>').text(dataJson[item]['id'])
    var hora = $('<p/>').text(dataJson[item]['data/hora'])
    var dono = $('<p/>').text(dataJson[item]['dono'])
    var cpf_cliente = $('<p/>').text(dataJson[item]['cpf_cliente'])
    var procedimento_clinico = $('<p/>').text(dataJson[item]['procedimento_clinico'])
    var procedimento_estetico = $('<p/>').text(dataJson[item]['procedimento_estetico'])
    var responsavel = $('<p/>').text(dataJson[item]['responsavel'])
    var status_atendimento = $('<p/>').text(dataJson[item]['status_atendimento'])
    notificacao.append(hora, dono, procedimento_clinico, procedimento_estetico,responsavel,status_atendimento)
  }
  console.log(dataJson)
})
