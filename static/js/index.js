 $("#login-button").click(function(event){
		 event.preventDefault();
	 if($('#username').val() == 'admin')
	 {
	 $('form').fadeOut(500);
	 $('.wrapper').addClass('form-success');
	 window.location.href = "home.html";
	 }
});

