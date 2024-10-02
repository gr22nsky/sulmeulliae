document.getElementById("signin-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessageElement = document.getElementById("error-message");

    try {
        console.log("로그인 요청 중...");

        // 백엔드로 로그인 요청
        const response = await axios.post('http://localhost:8000/api/v1/accounts/signin/', {
            username,
            password
        });

        // 요청 성공 시 토큰을 로컬 스토리지에 저장
        if (response.status === 200) {
            console.log("로그인 성공! 페이지 이동 중...");
            localStorage.setItem('access', response.data.access);

            // 성공 시 페이지 이동
            window.location.href = "/index.html";
        }
    } catch (error) {
        console.error("로그인 실패:", error);
        errorMessageElement.textContent = "Invalid credentials. Please try again.";
    }
});

