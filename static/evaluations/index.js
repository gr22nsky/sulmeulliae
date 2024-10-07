// API 엔드포인트 URL 설정
const API_URL = 'https://api.sulmeulliae.com/api/v1/evaluations/';
const USER_INFO_URL = 'https://api.sulmeulliae.com/api/v1/accounts/info/';  // 사용자 정보 가져오는 API URL

// 데이터 목록을 표시할 HTML 요소
const evaluationList = document.getElementById('evaluation-list');
const authButtons = document.getElementById('auth-buttons');

// 로컬 스토리지에서 JWT 토큰 가져오기
const access = localStorage.getItem('access');

// 사용자 정보를 가져와서 화면에 표시하는 함수
const fetchUserInfo = async () => {
    try {
        // JWT 토큰이 있을 경우 사용자 정보 가져오기
        if (access) {
            const response = await axios.get(USER_INFO_URL, {
                headers: {
                    Authorization: `Bearer ${access}`
                }
            });

            const user = response.data;
            // 로그인 시 사용자 이름 표시
            authButtons.innerHTML = `<p>${user.username}님 환영합니다!</p><button id="signout-btn">Sign Out</button>`;

            document.getElementById("signout-btn").addEventListener("click", () => {
                localStorage.removeItem('access');  // 로컬 스토리지에서 토큰 삭제
                window.location.href = '/index.html';  // 로그인 페이지로 이동
            });
        }
    } catch (error) {
    }
};

// API에서 데이터를 가져와 화면에 표시하는 함수
const fetchEvaluations = async () => {
    try {
        // Axios로 API 요청
        const response = await axios.get(API_URL);

        // API로부터 받은 데이터
        const evaluations = response.data;

        // 데이터를 HTML로 변환하여 화면에 표시
        evaluations.forEach(evaluation => {
            const evaluationItem = document.createElement('div');
            evaluationItem.className = 'evaluation-item';
            evaluationItem.innerHTML = `
                <a href='/evaluations/evaluationdetail.html?id=${evaluation.id}'>${evaluation.title}</a>
            `;
            evaluationList.appendChild(evaluationItem);
        });
    } catch (error) {
    }
};

// 페이지 로드 시 사용자 정보와 평가 목록 가져오기
window.onload = () => {
    fetchUserInfo();
    fetchEvaluations();
};
