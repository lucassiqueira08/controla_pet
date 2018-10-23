console.log('teste')
$('#achar_animal').click(function(){

	cpf_cliente = $('#cpf_cliente').val()
	nome_animal = $('#nome_animal').val()

	$.getJSON('/cliente/get_ficha_animal'+ '/' + cpf_cliente + 	'/' + nome_animal , function (data) {
		console.log(data) 
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
