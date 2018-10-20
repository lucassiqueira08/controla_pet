/*  TIPOS DE MENSAGEM:
      ¬ informacao
      ¬ erro
      ¬ aviso
      ¬ ok
*/
function alerta(mensagem, tipoMensagem, tempo){
  switch(tipoMensagem){
    case 'informacao':
      //INFORMAÇÃO
      $.toast({
          heading: 'Olha isso!',
          text: mensagem,
          showHideTransition: 'slide',
      	  position: 'top-right',
          hideAfter:tempo,
          icon: 'info'
      })
      break;

    case 'erro':
      //ERRO
      $.toast({
          heading: 'Erro...',
          text: mensagem,
          showHideTransition: 'fade',
          position: 'top-right',
          hideAfter:tempo,
          icon: 'error'
      })
      break;

    case 'aviso':
      //AVISO
      $.toast({
          heading: 'Aviso!',
          text: mensagem,
          showHideTransition: 'plain',
          position: 'top-right',
          hideAfter:tempo,
          icon: 'warning'
      })
      break;

    case 'ok':
      //SUCESSO
      $.toast({
          heading: 'Sucesso!',
          text: mensagem,
          showHideTransition: 'slide',
      	  position: 'top-right',
          hideAfter:tempo,
          icon: 'success'
      })
      break;
  }
}
