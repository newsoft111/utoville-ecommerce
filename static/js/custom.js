$(document).ready(function() {
	// a href='#' 클릭 무시 스크립트
	$('a[href="#"]').click(function(ignore) {
	   ignore.preventDefault();
	});
 });
 
window.onbeforeunload = function () { $('#my-spinner').show(); }  //현재 페이지에서 다른 페이지로 넘어갈 때 표시해주는 기능

$(window).load(function () {          //페이지가 로드 되면 로딩 화면을 없애주는 것
	$('#my-spinner').hide();
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

 $(document).ready(function(){

	$('.input-daterange').datepicker({
		format: 'dd-mm-yyyy',
		todayHighlight: true,
		startDate: '0d'
	});
	
});


