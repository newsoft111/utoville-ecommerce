$(document).ready(function() {
	// a href='#' 클릭 무시 스크립트
	$('a[href="#"]').click(function(ignore) {
	   ignore.preventDefault();
	});
 });
 
 function isEmpty(str){
		  
	if(typeof str == "undefined" || str == null || str == "")
		  return true;
	else
		  return false ;
 }
 
 function openModal(subject, content, before_modal, option) {
	$("#modal_subject").text(subject);
	$("#modal_content").html(content);
	if (!isEmpty(before_modal)) {
	   $('#closeModalBtn').attr('data-before-modal',before_modal);
	}
	if (option == 'reload') {
	   document.querySelectorAll('#closeModalBtn').forEach(function(close_btn) {
		  close_btn.setAttribute( "onClick", "window.location.reload();" );
	   });
	} else if (option == 'back') {
	   document.querySelectorAll('#closeModalBtn').forEach(function(close_btn) {
		  close_btn.setAttribute( "onClick", "history.back();" );
	   });
	} else if (isEmpty(option)) {
	   console.log('ok');
	} else {
	   document.querySelectorAll('#closeModalBtn').forEach(function(close_btn) {
		  close_btn.setAttribute( "onClick", `${option}` );
	   });
	}
	
	var modal = new bootstrap.Modal(document.getElementById('globalModal'))
	modal.show()
 }
 
function closeModal() {
	var before_modal = $('#closeModalBtn').attr('data-before-modal');
	$("#modal_subject").text('');
	$("#modal_content").html('');
	if (before_modal) {
		$(before_modal).modal('show');
	}
	
	$('#closeModalBtn').attr('data-before-modal','');
	var modal = new bootstrap.Modal(document.getElementById('globalModal'));
	modal.hide();
}



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}