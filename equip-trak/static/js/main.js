$(document).ready(function() {
	$('#userName').keyup(function() {
		var data = $('#regForm').serialize();
		$.ajax({
			method: 'POST',
			url: '/username',
			data: data
		}).done(function(res) {
			$('#userNameMsg').html(res);
		});
	});
	console.log('working');
	function navBar() {
		console.log('working');
		$.ajax({
			url: '/nav'
		}).done(function(res) {
			$('nav').html(res);
		});
	}

	navBar();
	$('#checkEquip #equipId').keyup(function() {
		var data = $('#checkEquip').serialize();
		$.ajax({
			method: 'POST',
			url: '/getEquip',
			data: data
		}).done(function(res) {
			console.log(res);
			$('#checkoutForm').html(res);
		});
	});
});
