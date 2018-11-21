$.getJSON('/usuario/get_cargo', function (data) {
    var selectCargos = $('#cargos')
    var cargos = data
    for (var cargo in cargos) {
        var option = $('<option/>').val(cargos[cargo].pk)
            .text(cargos[cargo].fields.nome)
        selectCargos.append(option)
    }
})

// Ajax - POST
$('#formcadastroFuncionario').on('submit', function (e) {
  e.preventDefault()
  var data = new FormData($('#formcadastroFuncionario').get(0));
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  $.ajax({
          type: "POST",
          url: '/usuario/cadastro_funcionario/',
          headers:{"X-CSRFToken": csrftoken},
          data:data,
          processData: false,
          contentType: false,
          dataType: "json",
          success: function (data) {
            alerta(data.mensagem, data.tipo, data.time)
            if (data.tipo=='ok') {
              $('#formcadastroFuncionario').each(function(){
                this.reset()
              })
            }
          },
          error:function (data) {
            alerta('Erro Interno!', 'erro', 7000)
          }
      })
})


$(document).ready(function () {
    $('input[name=veterinario]').change(function () {
        if ($("input[name='veterinario']:checked").val() == '1') {
            $("#crmv").removeClass(" hide")
            $("#emissor").removeClass(" hide")
        }
        if ($("input[name='veterinario']:checked").val() == '0') {
            $("#crmv").addClass(" hide")
            $("#emissor").addClass(" hide")
        }
    });
});
