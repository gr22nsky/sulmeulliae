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
        errorMessageElement.textContent = "Passwords do not match!";
        return;
    }

    // 생년월일 형식 확인 (YYYY-MM-DD)
    const birthRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!birthRegex.test(birth)) {
        errorMessageElement.textContent = "Birth date must be in the format YYYY-MM-DD";
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
            alert("Sign up successful! Please log in.");
            window.location.href = "/static/accounts/signin.html";
        }
    } catch (error) {
        console.error(error);
        errorMessageElement.textContent = "Failed to sign up. Please try again.";
    }
});
