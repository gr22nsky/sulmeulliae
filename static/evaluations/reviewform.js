document.getElementById("review-form").addEventListener("submit", async function(event) {
    event.preventDefault();  // 폼의 기본 제출 동작 막기

    const content = document.getElementById("review-content").value;
    const rating = document.getElementById("review-rating").value;
    const evaluationId = new URLSearchParams(window.location.search).get('id');  // URL에서 평가 ID 추출
    const access = localStorage.getItem('access');  // 저장된 JWT 토큰 가져오기

    try {
        const response = await axios.post(`https://sulmeulliae.com/api/v1/evaluations/${evaluationId}/review/`, {
            content: content,
            rating: rating
        }, {
            headers: {
                Authorization: `Bearer ${access}`,  // 인증 토큰 추가
                'Content-Type': 'application/json'
            }
        });

        if (response.status === 201) {
            alert('리뷰작성이 완료되었습니다!');
            // 리뷰가 성공적으로 제출되면 리뷰 리스트를 다시 로드하거나 페이지를 새로고침
            location.reload();  // 페이지 새로고침으로 리뷰 목록 업데이트
        }
    } catch (error) {
        alert('리뷰작성실패 다시시도해주세요.');
    }
});
