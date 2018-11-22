$(document).ready(function() {
	$('.ex1').each(function(index, el) {
		$(this).slider({
			tooltip:"show",
			formatter: function(value) {
				return 'Current value: ' + value;
			}
		});
		$(this).on("slide", function(slideEvt) {
			// console.log($(this).siblings('.sliderVal'));
			$(this).siblings('.sliderVal').text(slideEvt.value);
		});
	});
		
});