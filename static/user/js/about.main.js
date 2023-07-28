$(function(){
	var n=0;
	var t=0;
	var pos=0;
	var timer=0;
	var sum=0;
	var speedGap=200;

	$(".controller li").eq(0).addClass("on");

	$(window).on("scroll", function(){
		clearTimeout(timer);

		timer=setTimeout(function(){
			t=$(window).scrollTop();
			sum+=1;

			if(t < $("#page2").offset().top-speedGap){
				n=0;
			}
			else if(t < $("#page3").offset().top-speedGap){
				n=1;
			}
			else if(t < $("#page4").offset().top-speedGap){
				n=2;
			}
			else if(t < $("#page5").offset().top-speedGap){
				n=3;
			}
			else{
				n=4;
			}

			$(".controller li").removeClass("on");
			$(".controller li").eq(n).addClass("on");
		});
	});
	$(window).trigger("scroll");

	
	$(".controller li").on("click", function(e){
		e.preventDefault();
		n=$(this).index();
		

		if(n == 0){
			pos=$("#page1").offset().top-120;
		}
		else{
			pos=$("#page"+(n+1)).offset().top-120;
		}
		console.log(pos)
		$("body").animate({scrollTop:pos}, 800);
	});
	
	$(".btn_top").on("click", function(e){
		e.preventDefault();
		$("body").animate({scrollTop:0}, 400);
	});

});