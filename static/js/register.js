

  $(function() {
    $('[name="user_id"]').blur(function() {
        var user_id=$('[name="user_id"]').val()
        
        document.getElementById("id_error").innerHTML="";

        $.ajax({
            type: "POST",
            url: "/api/v1/id-validation",
            data: {'user_id' : user_id},
            success: function(response) {

                if (response.data == "exist") {
                    document.getElementById("id_error").innerHTML=
                    "중복되는 아이디 입니다. 다른 아이디를 사용해주세요.";
                }
                else {
                    document.getElementById("id_error").innerHTML=
                    "";
                }
                },
                error: function(error) {
                    console.log("ID validation error!");
                }
            });
          });
        });


  $(function() {
    $('[name="user_email"]').blur(function() {
        var user_email=$('[name="user_email"]').val()

        $.ajax({
            type: "POST",
            url: "/api/v1/email-validation",
            data: {'user_email' : user_email},
            success: function(response) {
                if (response.data == "exist") {
                    document.getElementById("email_error").innerHTML=
                    "중복되는 이메일입니다. 아이디 찾기를 이용해주세요.";
                }
                else{
                    document.getElementById("email_error").innerHTML=
                    "";
                }
              },
              error: function(error) {
                console.log("Email validation error!");
              }
            });
          });
        });
        
// 비밀번호 확인
$(function() {
    $('[name="password1"]').blur(function() {
        var password1=$('[name="password1"]').val()
        var password2=$('[name="password2"]').val()

        if (password1 == password2) {
            document.getElementById("pw1_error").innerHTML=
            "";
        }
        else {
            document.getElementById("pw1_error").innerHTML=
            "비밀번호가 일치하지 않습니다.";
        }
    });
});
