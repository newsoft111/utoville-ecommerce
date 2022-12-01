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
	document.getElementById("modal_subject").innerText = subject;
	document.getElementById("modal_content").innerHTML = content;
	// $("#modal_subject").text(subject);
	// $("#modal_content").html(content);
	if (!isEmpty(before_modal)) {
		document.querySelector('#closeModalBtn').dataset.beforeModal = before_modal;
		var modal = bootstrap.Modal.getOrCreateInstance(document.querySelector(before_modal));
		modal.hide();
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
	var before_modal = document.querySelector('[id=closeModalBtn]').dataset.beforeModal;
	if (!isEmpty(before_modal)) {
		bootstrap.Modal.getOrCreateInstance(document.querySelector(before_modal)).show();
	}
	document.querySelector("[id=modal_subject]").innerHTML = '';
	document.querySelector("[id=modal_content]").innerHTML = '';
	
	document.querySelector('[id=closeModalBtn]').dataset.beforeModal = '';

	var modal = bootstrap.Modal.getOrCreateInstance(document.getElementById('globalModal'));
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

function numberWithCommas(num) { 
	var parts = num.toString().split("."); 
	return parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",") + (parts[1] ? "." + parts[1] : ""); 
}

function isDuplicate(arr) {
	const isDup = arr.some(function(x) {
	  return arr.indexOf(x) !== arr.lastIndexOf(x);
	});
						   
	return isDup;
}