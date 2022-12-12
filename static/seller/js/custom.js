function isEmpty(str){
	if(typeof str == "undefined" || str == null || str == "")
		return true;
	else
		return false ;
}
 
 function openModal(subject, content, before_modal_id, option) {
	document.querySelector("[id=modal_subject]").innerHTML = subject;
	document.querySelector("[id=modal_content]").innerHTML = content;

	if (!isEmpty(before_modal_id)) {
		document.querySelector('#closeModalBtn').dataset.beforeModal = before_modal_id;
		var modal = bootstrap.Modal.getOrCreateInstance(document.querySelector(before_modal_id));
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
	
	var modal = bootstrap.Modal.getOrCreateInstance(document.getElementById('globalModal'));
	modal.show();
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


function serialize (rawData) {
	
	let rtnData = {};
	for (let [key, value] of rawData) {
		let sel = document.querySelectorAll("[name=" + key + "]");
	
		// Array Values
		if (sel.length > 1) {
			if (rtnData[key] === undefined) {
				rtnData[key] = [];				
			}
			rtnData[key].push(value);
		} 
		// Other 
		else {
        	rtnData[key] = value;
		}
	}
	
	return rtnData;
}

function numberWithCommas(num) { 
	var parts = num.toString().split("."); 
	return parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",") + (parts[1] ? "." + parts[1] : ""); 
}

// 이메일 정규표현식
function email_check(email) {
    let regex=/([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    return (email != '' && email != 'undefined' && regex.test(email));   // 정규표현식 검사를 통과하면 true를 리턴
}
// 계좌번호 정규표현식
function account_check(number) {
	let regex = /^[0-9]{4}[-\s\.]?[0-9]{4}[-\s\.]?[0-9]{4}[-\s\.]?[0-9]{4}$/;  //(임시) 카드번호 4자리-4자리-4자리-4자리 유형 체크
	return (number != '' &&  number != 'undefined' && regex.test(number));
}
// 비밀번호 정규표현식
function password_check(number) {
	let regex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/;
	return (number != '' &&  number != 'undefined' && regex.test(number));
}