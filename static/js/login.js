$(function() {
    $('#signUp').click(function() {
        var uid = $('#bitsID').val();
        var name = $('#name').val();
        var password = $('#password').val();
        var cpassword = $('#cpassword').val();
        var phno = $('#phno').val();
        var roomno = $('#roomno').val();
        var fbid = $('#fbid').val();
        $.ajax({
            url: '/dashboard/',         //dashboard is just for testing, have to change it later to /signup/
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});