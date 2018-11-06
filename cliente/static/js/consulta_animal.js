console.log('teste')
	
$('#achar_animal').on('click', function(e) {
  e.preventDefault()
  var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
  	cpf_cliente = $('#cpf_cliente').val()
	nome_animal = $('#nome_animal').val()
  $.ajax({
          type: "GET",
          url: '/cliente/get_ficha_animal'+ '/' + cpf_cliente + 	'/' + nome_animal,
          headers:{
              "X-CSRFToken": csrftoken,
          },
          data:{},
          success: function (data) 
          {
            if (data.tipo=='erro') {
              $('#voltar').click()	
              alerta(data.mensagem, data.tipo, data.time)
              let timerId = setInterval(() => window.location.reload(), data.time);
            }
            else{
         		$('#nome').val(data[0].fields.nome)
				$('#raca').val(data[0].fields.raca)
				$('#dono').val(data[0].fields.nome)

            }

           
          }
        })
  })