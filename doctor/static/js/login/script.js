$(function () {
    $('.forgotBtn').click(function () {
        $('#forgot').toggleClass('toggle')
    })

    $('.registerBtn').click(function () {
        $('#register, #formContainer').toggleClass('toggle')
    })

    $('#login-button').click(function (){
        let username = $('#name-input').val()
        let password = $('#password-input').val()

        $.ajax({
            url:"http://127.0.0.1:8000/getinfo/",
            type:"GET",
            data:{
                platform: "web",
            },
            success: function (resp) {
                if(resp.result == "success" && resp.username==username && resp.password==password){
                    window.location.href='http://127.0.0.1:8000/user';
                }else{
                    alert("用户名或密码有错误")
                }
            }
        })
    })
})