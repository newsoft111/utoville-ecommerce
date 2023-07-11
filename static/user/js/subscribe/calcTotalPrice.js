let addOptionContent = document.querySelector(".add_option_content");
let hasInputOption = addOptionContent.querySelectorAll(".has_input_option");
let noneInputOption = addOptionContent.querySelectorAll(".none_input_option")
let subscribeTotalPrice = document.querySelector(".subscribe_total_price .payment");
let basicOptionPrice = Number(subscribeTotalPrice.innerHTML.replace(/[^\d.-]/g, ''));
let qty = null;

import { inputOptionPrices, nonInputOptionPrices } from "/static/user/js/subscribe/optionData.js";

export function calcTotalPrice(e) {

	// console.log(inputOptionPrices[i].id, nonInputOptionPrices[i].id)

	let totalPrice = 0;
	let optionName = [];
	let noneInputOptionName = [];
	let inputOptionSubTotals = [];
	let noneInputOptionSubTotals = [];
	let count = [];
	let html = "";

	hasInputOption.forEach((option, i) => {
		option.index = i;  // hasInputOption 각각의 요소 값 i를 index값에 동적 할당
		optionName.push(option.querySelector("input[type=number]").name);
		let qty = option.querySelector("input[type=number").value;
		let optionPrice = inputOptionPrices[i][optionName[i]];
		let optionTotalPrice = parseFloat(qty * optionPrice);

		count.push(Number(qty));
		totalPrice += optionTotalPrice;

		inputOptionSubTotals.push(optionTotalPrice);

	});

	noneInputOption.forEach((option, i) => {
		option.index = i;
		
		noneInputOptionName.push(option.querySelector("input[type=hidden]").name);

		let noneInputOptionPrice = nonInputOptionPrices[i][noneInputOptionName[i]];
		let optionTotalPrice = parseFloat(noneInputOptionPrice);

		noneInputOptionSubTotals.push(optionTotalPrice);
	});

	// optionData.js 에 저장된 데이터 id와 현재 선택된(e.currentTarget) index(option.index = i 를 통해 index값 동적 할당)값이 같은 항목을 return하여 inputPk 변수에 저장
	let inputPk = inputOptionPrices.find(function(data){
		return data.id == e.currentTarget.index
	});

	let noneInputPk = nonInputOptionPrices.find(function(data){
		return data.id == e.currentTarget.index
	})

	// 이전에 선택한 옵션의 가격 업데이트
	let existingOptionElement  = '';
	if(e.currentTarget.querySelector("input").type === "number"){
		existingOptionElement = document.querySelector(`.add_order_list [data-index="${inputPk.id}"]`);
	}
	if(e.currentTarget.querySelector("input").type === "hidden"){
	 	existingOptionElement = document.querySelector(`.add_order_list [data-noneOptionIndex="${noneInputPk.id}"]`);
	}

	if (existingOptionElement) {
		let existingPriceElement = existingOptionElement.querySelector(".option-price");
		let noneOptionPirceElement = existingOptionElement.querySelector(".none-option-price");
		let qtyElement = existingOptionElement.querySelector(".option-qty span");

	// number 옵션과 hidden 옵션을 함께 처리
		if(e.currentTarget.querySelector("input[type=number]")){
			qtyElement.textContent = `(${count[e.currentTarget.index]})`;
			existingPriceElement.textContent = `₱ ${numberWithCommas(inputOptionSubTotals[e.currentTarget.index].toFixed(2))}`;
		}else if(e.currentTarget.classList.contains("fill")){
			noneOptionPirceElement.textContent = `₱ ${numberWithCommas(noneInputOptionSubTotals[e.currentTarget.index].toFixed(2))}`;
		}else{
			existingOptionElement.remove();
		}

	} else {
		let html = '';
		if(e.currentTarget.querySelector("input").type === "number"){
			html = `
				<div class="d-flex justify-content-between py-2" data-index="${e.currentTarget.index}" style="border-bottom: 1px solid #ddd;">
					<p class="option-qty mb-0">+ ${optionName[e.currentTarget.index]}<span>(${count[e.currentTarget.index]})</span></p>
					<span class="option-price">₱ ${numberWithCommas(inputOptionSubTotals[e.currentTarget.index].toFixed(2))}</span>
				</div>
			`; 
		}
		
		if(e.currentTarget.querySelector("input").type === "hidden" && e.currentTarget.classList.contains("fill")){
			html = `
				<div class="d-flex justify-content-between py-2" data-noneOptionindex="${e.currentTarget.index}" style="border-bottom: 1px solid #ddd;">
					<p class="option-qty mb-0">+ ${noneInputOptionName[e.currentTarget.index]}</p>
					<span class="none-option-price">₱ ${numberWithCommas(noneInputOptionSubTotals[e.currentTarget.index].toFixed(2))}</span>
				</div>
			`;
		}

		document.querySelector(".add_order_list").insertAdjacentHTML("beforeend", html);
	}

	// 수량 선택 없는 옵션 선택에 대한 이벤트
	
	let selectedHiddenOptions = [];

	noneInputOption.forEach((option, i) => {
		noneInputOptionName.push(option.querySelector("input[type=hidden]").name);
		let noneInputOptionPrice = nonInputOptionPrices[i][noneInputOptionName[i]];

		noneInputOptionSubTotals.push(Number(noneInputOptionPrice));

		if (option.classList.contains("fill")) {
			selectedHiddenOptions.push(i);  // 옵션이 선택되어 색이 변경될때 해당 옵션의 i값을 selectedHiddenOptions 배열에 저장
		}
	});

	let selectedHiddenOptionsTotalPrice = selectedHiddenOptions.reduce((total, index) => {  // 배열에 저장된 선택된 옵션의 갯수만큼 reduce 함수 실행
		return total + noneInputOptionSubTotals[index]; // 초기값을 0으로 설정하여 누적값을 초기화하고 현재 요소의 가격을 total에 더함
	}, 0);
	
	totalPrice += selectedHiddenOptionsTotalPrice;
	
	if(totalPrice == 0){
		subscribeTotalPrice.innerHTML = "₱ 499.00";
		document.querySelector(".basic_option_price").innerHTML = "";
	}else{
		html = `
				<p class="basic-option-price py-2 mb-0 text-end">₱ 499.00</p>
			`;
		document.querySelector(".basic_option_price").innerHTML = html;
		subscribeTotalPrice.innerHTML = "₱ " + numberWithCommas((basicOptionPrice+totalPrice).toFixed(2));
	}
}