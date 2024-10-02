document.getElementById("signup-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    

    const fullname = document.getElementById("fullname").value;
    const nickname = document.getElementById("nickname").value;
    const birth = document.getElementById("birth").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    const errorMessageElement = document.getElementById("error-message");

    // 비밀번호 확인
    if (password !== confirmPassword) {
        errorMessageElement.textContent = "비밀번호가 일치하지 않습니다.";
        return;
    }

    // 생년월일 형식 확인 (YYYY-MM-DD)
    const birthRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!birthRegex.test(birth)) {
        errorMessageElement.textContent = "생년월일 형식이 맞지 않습니다.";
        return;
    }

    try {
        // 백엔드로 회원가입 요청
        const response = await axios.post('http://localhost:8000/api/v1/accounts/', {
            fullname,
            nickname,
            birth,
            username,
            email,
            password
        });
        if (response.status === 200) {
            alert("회원가입이 완료되었습니다 로그인하세요.");
            window.location.href = "/static/accounts/signin.html";        
        }
    } catch (error) {
        console.error(error);
        errorMessageElement.textContent = "회원가입에 실패하였습니다. 다시시도하세요.";
    }
});
