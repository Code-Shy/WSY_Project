$(function (){
    $('#register-button').click(function (){
        let username = $('#register-input-name').val()
        let email = $('#register-input-email').val()
        let password = $('#register-input-password').val()
        let repassword = $('#register-input-repassword').val()

        if(username === ""){
            alert("用户名不能为空")
        }else if(email === ""){
            alert("邮箱不能为空")
        }else if(password === ""){
            alert("密码不能为空")
        }else if(repassword === ""){
            alert("请再次输入密码")
        }

        $.ajax({
            url:"http://127.0.0.1:8000/register/",
            type:'GET',
            data: {
                username:username,
                password:password,
                email:email,
            },
            success: function (resp){
                if(resp.result === "success"){
                    alert("注册成功")
                    window.location.href='http://127.0.0.1:8000/user';
                }else{
                    alert("注册失败")
                }
            }
        })
    })
})