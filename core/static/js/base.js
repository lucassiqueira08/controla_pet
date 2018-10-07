$.get('/get_notificacao', function(data){
  var notificacoes = $('#notificacoes')
  var notificacao  =
                     '<div class="card card-body">'
                   +   '<ul>'
                   +     '<li class="notificacao">'
                   +       '<p class="notificacaoHorario">##hora</p>'
                   +       '<p class="notificacaoBichinho">##bichinho</p>'
                   +       '<p class="notificacaoProcedimento">##procedimento</p>'
                   +     '</li>'
                   +   '</ul>'
                   + '</div>';
  dataJson = JSON.parse(data)


  for (var item in dataJson) {
    var id                    = dataJson[item]['id'];
    var data                  = (dataJson[item]['data/hora']).substring(0,10).replace("-","/");
    var hora                  = (dataJson[item]['data/hora']).substring(11,16);
    var dono                  = dataJson[item]['dono'];
    var cpf_cliente           = dataJson[item]['cpf_cliente'];
    var procedimento_clinico  = dataJson[item]['procedimento_clinico'];
    var procedimento_estetico = dataJson[item]['procedimento_estetico'];
    var responsavel           = dataJson[item]['responsavel'];
    var status_atendimento    = dataJson[item]['status_atendimento'];

    var procedimento          = dataJson[item]['procedimento_clinico'] != null ? dataJson[item]['procedimento_clinico'] : dataJson[item]['procedimento_estetico'] != null ? dataJson[item]['procedimento_estetico'] : "Sem procedimento!";
    var final                 = notificacao.replace("##hora", hora).replace("##bichinho",dono).replace("##procedimento",procedimento);

    notificacoes.append(final)
  }
  console.log(dataJson)
})

function verifica_horario_notificacao(){
  var d           = new Date();
  var hora_atual  = d.toString().substring(16,24);

  for (var item in dataJson) {
    var hora  = (dataJson[item]['data/hora']).substring(11,19);
    if (hora == hora_atual) {
      alerta("ta na hora!","aviso",7000);
    }

  }
}
let timerId = setInterval(() => verifica_horario_notificacao(), 1000);
