const fetchReviewList = async (evaluationId) => {
    try {
        const response = await axios.get(`http://localhost:8000/api/v1/evaluations/${evaluationId}/review/`, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('access')}`,  // 토큰 가져오기
            },
        });
        const reviews = response.data;
        let reviewsHtml = '';
        reviews.forEach(review => {
            reviewsHtml += `
                <div class="review">
                    <p>${review.author} | ${review.content} | ${review.rating} 점</p>
                </div>
            `;
        });

        const reviewSection = document.getElementById('review-list');
        if (reviewSection) {
            reviewSection.innerHTML = reviewsHtml;
        }
    } catch (error) {
        console.error('Error fetching reviews:', error);

        if (error.response && error.response.status === 401) {
            alert('로그인후 이용해주세요.');
            window.location.href = "/accounts/signin.html";
        }
    }
};

// `DOMContentLoaded` 이벤트로 페이지가 완전히 로드된 후 실행
document.addEventListener('DOMContentLoaded', () => {
    const evaluationId = new URLSearchParams(window.location.search).get('id');
    fetchReviewList(evaluationId);
});
