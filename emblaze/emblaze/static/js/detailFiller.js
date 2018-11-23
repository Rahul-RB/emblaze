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
	
	$(".citySearch").each(function(index, el) {
		var $this = $(this);
		$(this).on('input', function(event) {
			$(".searchResults").empty();
			event.preventDefault();
			/* Act on the event */
			if($(this).val().length >=3){
				var inpData = {
					search : $(this).val(),
					infoType : "cities"
				}
				$.ajax({
					url: 'getInfo',
					type: 'GET',
					dataType: 'json',
					data: inpData,
				})
				.done(function(data) {
					console.log("<GET-1>success\n",data);
					console.log("$this\n",$this);
					var $thisSibling = $this.siblings(".searchResults");
					console.log("$thisSibling\n",$thisSibling);
					
					$.each(data, function(index, val) {
						console.log(val);
						$thisSibling.append("<div class='searchRes' style='background-color:grey;cursor:pointer;margin-bottom:1px;'>"+val+"</div>");
						$(".searchRes").each(function(index,el2){
							$(this).on('click', function(event) {
								event.preventDefault();
								/* Act on the event */
								console.log("Res:",$(this).text());
								$this.val($(this).text());
								$(this).parent(".searchResults").empty()
							});
						});	
					});
				})
				.fail(function() {
					console.log("error");
				})
				.always(function() {
					console.log("complete");
				});
			}	
		});
	});

	$(".stateSearch").each(function(index, el) {
		var $this = $(this);
		$(this).on('input', function(event) {
			$(".stateSearchResults").empty();
			event.preventDefault();
			/* Act on the event */
			if($(this).val().length >=3){
				var inpData = {
					search : $(this).val(),
					infoType : "states"
				}
				$.ajax({
					url: 'getInfo',
					type: 'GET',
					dataType: 'json',
					data: inpData,
				})
				.done(function(data) {
					console.log("<GET-1>success\n",data);
					console.log("$this\n",$this);
					var $thisSibling = $this.siblings(".stateSearchResults");
					console.log("$thisSibling\n",$thisSibling);
					
					$.each(data, function(index, val) {
						console.log(val);
						$thisSibling.append("<div class='searchRes' style='background-color:grey;cursor:pointer;margin-bottom:1px;'>"+val+"</div>");
						$(".searchRes").each(function(index,el2){
							$(this).on('click', function(event) {
								event.preventDefault();
								/* Act on the event */
								console.log("Res:",$(this).text());
								$this.val($(this).text());
								$(this).parent(".stateSearchResults").empty()
							});
						});	
					});
				})
				.fail(function() {
					console.log("error");
				})
				.always(function() {
					console.log("complete");
				});
			}	
		});
	});

	$(".companySearch").each(function(index, el) {
		var $this = $(this);
		$(this).on('input', function(event) {
			$(".companySearchResults").empty();
			event.preventDefault();
			/* Act on the event */
			if($(this).val().length >=3){
				var inpData = {
					search : $(this).val(),
					infoType : "companies"
				}
				$.ajax({
					url: 'getInfo',
					type: 'GET',
					dataType: 'json',
					data: inpData,
				})
				.done(function(data) {
					console.log("<GET-1>success\n",data);
					console.log("$this\n",$this);
					var $thisSibling = $this.siblings(".companySearchResults");
					console.log("$thisSibling\n",$thisSibling);
					
					$.each(data, function(index, val) {
						console.log(val);
						$thisSibling.append("<div class='searchRes' style='background-color:grey;cursor:pointer;margin-bottom:1px;'>"+val+"</div>");
						$(".searchRes").each(function(index,el2){
							$(this).on('click', function(event) {
								event.preventDefault();
								/* Act on the event */
								console.log("Res:",$(this).text());
								$this.val($(this).text());
								$(this).parent(".companySearchResults").empty()
							});
						});	
					});
				})
				.fail(function() {
					console.log("error");
				})
				.always(function() {
					console.log("complete");
				});
			}	
		});
	});
});