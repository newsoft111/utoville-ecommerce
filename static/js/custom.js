function isEmpty(str){
		  
	if(typeof str == "undefined" || str == null || str == "")
		  return true;
	else
		  return false ;
 }
 
 function openModal(subject, content, before_modal, option) {
	document.querySelector("[id=modal_subject]").innerHTML = subject;
	document.querySelector("[id=modal_content]").innerHTML = content;
	if (!isEmpty(before_modal)) {
	   $('#closeModalBtn').attr('data-before-modal',before_modal);
	}
	if (option == 'reload') {
	   document.querySelectorAll('closeModalBtn').forEach(function(close_btn) {
		  close_btn.setAttribute( "onClick", "window.location.reload();" );
	   });
	} else if (option == 'back') {
	   document.querySelectorAll('closeModalBtn').forEach(function(close_btn) {
		  close_btn.setAttribute( "onClick", "history.back();" );
	   });
	} else if (isEmpty(option)) {
	   console.log('ok');
	} else {
	   document.querySelectorAll('closeModalBtn').forEach(function(close_btn) {
		  close_btn.setAttribute( "onClick", `${option}` );
	   });
	}
	
	var modal = new bootstrap.Modal(document.getElementById('globalModal'))
	modal.show()
 }
 
function closeModal() {
	var before_modal = document.querySelector('[id=closeModalBtn]').dataset.beforeModal;
	document.querySelector("[id=modal_subject]").innerHTML = '';
	document.querySelector("[id=modal_content]").innerHTML = '';
	if (!isEmpty(before_modal)) {
		before_modal = new bootstrap.Modal(document.querySelector('before_modal'));
		before_modal.show();
	}
	
	document.querySelector('[id=closeModalBtn]').dataset.beforeModal = '';
	var modal = new bootstrap.Modal(document.getElementById('globalModal'));
	modal.hide();
}



