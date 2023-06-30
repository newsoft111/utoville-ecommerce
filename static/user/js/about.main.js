$(function(){
	var n=0;
	var t=0;
	var pos=0;
	var timer=0;
	var sum=0;
	var speedGap=200;

	$("#main_slider").addClass("active");
	$(".controller li").eq(0).addClass("on");

	$(window).on("scroll", function(){
		t=$(window).scrollTop();

		if(t > 80) {
			$("#header").addClass("fixed");
		}
		else{
			$("#header").removeClass("fixed");
		}

		clearTimeout(timer);

		timer=setTimeout(function(){
			t=$(window).scrollTop();
			sum+=1;

			if(t < $("#page1").offset().top-speedGap){
				n=0;
			}
			else if(t < $("#page2").offset().top-speedGap){
				n=1;
			}
			else if(t < $("#page3").offset().top-speedGap){
				n=2;
			}
			else if(t < $("#page4").offset().top-speedGap){
				n=3;
			}
			else if(t < $("#page5").offset().top-speedGap){
				n=4;

			}
			else{
				n=5;
			}

			if(n == 0){
				$("#main_slider").addClass("active");
			}
			else{
				$("#page"+n).addClass("active");
			}

			$(".controller li").removeClass("on");
			$(".controller li").eq(n).addClass("on");
			$("#gnb li").removeClass("active");
			$("#gnb li").eq(n).addClass("active");
		});
	});
	$(window).trigger("scroll");

	$("#gnb li, #mobile li").on("click", function(e){
		e.preventDefault();
		n=$(this).index();

		if(n == 0){
			pos=$("#main_slider").offset().top;
		}
		else{
			pos=$("#page"+n).offset().top;
		}
		
		$("body").animate({scrollTop:pos}, 800);
		$("body").removeClass("fixed");
		$("#mobile").removeClass("active");
		$(".main_tab").removeClass("active");
		$(".dim").removeClass("active");
	});
	$(".controller li").on("click", function(e){
		e.preventDefault();
		n=$(this).index();

		if(n == 0){
			pos=$("#main_slider").offset().top;
		}
		else{
			pos=$("#page"+n).offset().top;
		}

		$("body").animate({scrollTop:pos}, 800);
	});
	$(".main_tab").on("click", function(e){
		e.preventDefault();

		$("#mobile").toggleClass("active");
		$(".main_tab").toggleClass("active");
		$(".dim").toggleClass("active");
	});
	$(".dim").on("click", function(){
		$("body").removeClass("fixed");
		$("#mobile").removeClass("active");
		$(".main_tab").removeClass("active");
		$(".dim").removeClass("active");
	});
	$(".btn_top").on("click", function(e){
		e.preventDefault();
		$("body").animate({scrollTop:0}, 400);
	});
	$(".portfolio_list li").mouseenter(function(){
		$(this).addClass("over");
	});
	$(".portfolio_list li").mouseleave(function(){
		$(".portfolio_list li").removeClass("over");
	});
});