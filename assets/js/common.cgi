#!/usr/bin/perl

if($ENV{'HTTP_REFERER'} eq ""){
	print "Content-type: text/html\n\n";
	print "You can not access file directly";
	exit;
}

print "Content-Type: application/x-javascript\n\n";

print <<__JS__;

\$(document).ready(function() {
	\$(document).gotopgoanchor({
	});
});
\$(function(){
	\$('.boxframe').addClass("heightLineParent");
});
\$(function(){
	\$("[gallary-area]").click(function(){
	var h=\$(this).attr("href");
	var t=\$(this).attr("gallary-area");
		\$(t).fadeOut(function(){
			(\$(t).attr("src",h)).fadeIn();
		});
		return false;
	})
});
\$(function(){
	\$("[data-featherlight] > img").wrap("<div class='thumbnail'>").after("<img class=zoom src=images/zoom.png />");
	\$("[gallary-area]:not(:has(img))").append("<img src=images/zoom.png valign=middle />");
	\$("[data-featherlight]:not(:has(img))").append("<img src=images/zoom.png valign=middle />");
});
\$(document).ready(function() {
	\$("dl.new").niceScroll({
		cursorcolor:"#888",
		cursorwidth:"10px",
		cursoropacitymin:1.0,
	});
});

__JS__
