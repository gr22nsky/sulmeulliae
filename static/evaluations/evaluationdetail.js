// URL에서 평가 ID 추출
const params = new URLSearchParams(window.location.search);
const evaluationId = params.get('id');

// API 엔드포인트 설정
const EVALUATION_DETAIL_URL = `https://api.api.sulmeulliae.com/api/v1/evaluations/${evaluationId}/`;

// 평가 상세 정보를 표시할 요소
const evaluationDetail = document.getElementById('evaluation-detail');

// 로컬 스토리지에서 JWT 토큰 가져오기
const access = localStorage.getItem('access');

// 평가 상세 정보를 API로부터 가져오는 함수
const fetchEvaluationDetail = async () => {
    try {
        // Authorization 헤더에 토큰을 추가하여 요청
        const response = await axios.get(EVALUATION_DETAIL_URL, {
            headers: {
                Authorization: `Bearer ${access}`  // JWT 토큰 추가
            }
        });

        const evaluation = response.data;
        let imagesHtml = '';
        evaluation.images.forEach(image => {
            imagesHtml += `<img src="https://api.sulmeulliae.com${image.image}" alt="${image.image}" />`;
        });
        evaluationDetail.innerHTML = `
            <h2>${evaluation.title}</h2>
            <p>${evaluation.content}</p>
            <div class="evaluation-images">${imagesHtml}</div>
            <p>${evaluation.origin}</p>
            <p>${evaluation.size}</p>
            <p>${evaluation.ingredient}</p>
            <p>주종: ${evaluation.category}</p>
            <p>도수: ${evaluation.ABV}%</p>
            <p>평점: ${evaluation.avg_rating}점</p>
            <p>조회수: ${evaluation.viewcounts}</p>
        `;
    } catch (error) {
        // 토큰이 유효하지 않거나 만료된 경우 처리
        if (error.response && error.response.status === 401) {
            alert('로그인후 이용해주세요.');
            window.location.href = "/static/accounts/signin.html";  // 로그인 페이지로 리디렉션
        }
    }
};
// 페이지 로드 시 평가 상세 정보 한 번만 가져오기
window.onload = () => {
    if (access) {  // 토큰이 있을 때만 요청
        fetchEvaluationDetail();
    } 
    else {
        alert('로그인후 이용해주세요.');
        window.location.href = "/accounts/signin.html";  // 토큰이 없으면 로그인 페이지로 이동
    }
};
