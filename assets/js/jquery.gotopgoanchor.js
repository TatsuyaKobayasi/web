(function($) {
	$.fn.gotopgoanchor = function(options){

	return this.each(function(){
		$("body").prepend("<div id='page_top' style='visibility:hidden'></div><div id='gotop'><a href='#page_top'>↑ページトップへ</a></div>");
		$('#gotop').hide();
		$(window).scroll(function(){
			if ($(this).scrollTop() > 150) {
				$('#gotop').fadeIn();
			}
			else {
				$('#gotop').fadeOut();
			}
		});
	 
		$('a[href^=#]').click(function() {
		  var speed = 400;
		  var href= $(this).attr("href");
		  var target = $(href == "#" || href == "" ? 'html' : href);
		  var position = target.offset().top;
		  $('body,html').animate({scrollTop:position}, speed, 'swing');
		  return false;
	   });
	});

	}
})(jQuery);