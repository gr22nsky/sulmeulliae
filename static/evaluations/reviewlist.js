const fetchReviewList = async (evaluationId) => {
    try {
        const response = await axios.get(`https://api.sulmeulliae.com/api/v1/evaluations/${evaluationId}/review/`, {
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
                    <button onclick="window.location.href='/evaluations/reviewedit.html?reviewId=${review.id}'">수정</button>
                    <button onclick="deleteReview(${review.id})">삭제</button>
                </div>
            `;
        });

        const reviewSection = document.getElementById('review-list');
        if (reviewSection) {
            reviewSection.innerHTML = reviewsHtml;
        }
    } catch (error) {
        if (error.response && error.response.status === 401) {
            alert('로그인후 이용해주세요.');
            window.location.href = "/accounts/signin.html";
        }
    }
};

const deleteReview = async (reviewId) => {
    const confirmDelete = confirm("Are you sure you want to delete this review?");
    if (confirmDelete) {
        try {
            const response = await axios.delete(`https://api.sulmeulliae.com/api/v1/evaluations/review/${reviewId}/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access')}`,
                }
            });

            if (response.status === 204) {
                alert('삭제되었습니다!');
                location.reload();  // 페이지 새로고침으로 리뷰 목록 업데이트
            }
        } catch (error) {
            alert('삭제실패 다시시도해주세요.');
        }
    }
};

// `DOMContentLoaded` 이벤트로 페이지가 완전히 로드된 후 실행
document.addEventListener('DOMContentLoaded', () => {
    const evaluationId = new URLSearchParams(window.location.search).get('id');
    fetchReviewList(evaluationId);
});
