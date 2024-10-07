document.getElementById("signin-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessageElement = document.getElementById("error-message");

    try {
        // 백엔드로 로그인 요청
        const response = await axios.post('https://api.sulmeulliae.com/api/v1/accounts/signin/', {
            username,
            password
        });

        // 요청 성공 시 토큰을 로컬 스토리지에 저장
        if (response.status === 200) {
            localStorage.setItem('access', response.data.access);
            // 성공 시 페이지 이동
            window.location.href = "/index.html";
        }
    } catch (error) {
        errorMessageElement.textContent = "로그인정보를 확인해주세요.";
    }
});

