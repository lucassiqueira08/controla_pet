$(document).ready(function() {
  hiddenClinica()
});


$('#Estadia').click(function () {
    $('#AnimaisHospedados_filter').css('display', 'block')
    $('#AnimaisHospedados_paginate').css('display', 'block')
    $('#AnimaisHospedados_length').css('display', 'block')
    $('#AnimaisHospedados_info').css('display', 'block')

    $('#AcompanheSuaClinica_filter').css('display', 'none')
    $('#PagamentosPendentes_filter').css('display', 'none')

    $('#AcompanheSuaClinica_paginate').css('display', 'none')
    $('#PagamentosPendentes_paginate').css('display', 'none')

    $('#AcompanheSuaClinica_length').css('display', 'none')
    $('#PagamentosPendentes_length').css('display', 'none')

    $('#AcompanheSuaClinica_info').css('display', 'none')
    $('#PagamentosPendentes_info').css('display', 'none')
})

$('#Pagamentos').click(function () {
    $('#PagamentosPendentes_filter').css('display', 'block')
    $('#PagamentosPendentes_paginate').css('display', 'block')
    $('#PagamentosPendentes_length').css('display', 'block')
    $('#PagamentosPendentes_info').css('display', 'block')

    $('#AcompanheSuaClinica_filter').css('display', 'none')
    $('#AnimaisHospedados_filter').css('display', 'none')

    $('#AnimaisHospedados_paginate').css('display', 'none')
    $('#AcompanheSuaClinica_paginate').css('display', 'none')

    $('#AcompanheSuaClinica_length').css('display', 'none')
    $('#AnimaisHospedados_length').css('display', 'none')

    $('#AnimaisHospedados_info').css('display', 'none')
    $('#AcompanheSuaClinica_info').css('display', 'none')
})

$('#Clinica').click(function () {
  hiddenClinica()
})

function hiddenClinica() {
  $('#AcompanheSuaClinica_paginate').css('display', 'block')
  $('#AcompanheSuaClinica_filter').css('display', 'block')
  $('#AcompanheSuaClinica_length').css('display', 'block')
  $('#AcompanheSuaClinica_info').css('display', 'block')

  $('#AnimaisHospedados_filter').css('display', 'none')
  $('#PagamentosPendentes_filter').css('display', 'none')

  $('#AnimaisHospedados_paginate').css('display', 'none')
  $('#PagamentosPendentes_paginate').css('display', 'none')

  $('#AnimaisHospedados_length').css('display', 'none')
  $('#PagamentosPendentes_length').css('display', 'none')

  $('#AnimaisHospedados_info').css('display', 'none')
  $('#PagamentosPendentes_info').css('display', 'none')
}



var AcompanheSuaClinica = $('#AcompanheSuaClinica').DataTable( {
    "processing": true,
    ajax: {
        "processing": true,
        url: '/servicos/get_atendimentos_pendentes',
        "dataSrc": ""
    },
    'columns': [
        { "data": "id_status__nome" },
        { "data": "id_atendimento__id_cliente__nome" },
        { "data": "id_atendimento__feitopor_atendimento__data_realizacao" },
    ]
} );

var AnimaisHospedados = $('#AnimaisHospedados').DataTable( {
    "processing": true,
    ajax: {
        "processing": true,
        url: '/servicos/get_animais_hospedados',
        "dataSrc": ""
    },
    'columns': [
        { "data": "id_status__nome_status" },
        { "data": "id_estadia__id_animal__nome" },
        { "data": "id_estadia__data_inicio" },
        { "data": "id_estadia__data_fim" },
    ]
} );

var PagamentosPendentes = $('#PagamentosPendentes').DataTable( {
    "processing": true,
    ajax: {
        "processing": true,
        "url": '/servicos/get_pagamentos_pendentes',
        "dataSrc": ""
    },
    'columns': [
        { "data": "id_atendimento__id_animal__id_cliente__id_tipo_cliente__nome" },
        { "data": "id_atendimento__id_animal__id_cliente__nome" },
        { "data": "id_atendimento__id_orcamento__preco_final" },
        { "data": "id_atendimento__feitopor_atendimento__data_realizacao" },
        { "data": "id_status__nome" },
    ]
} );
