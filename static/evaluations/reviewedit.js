// 기존 리뷰 데이터를 불러와 폼에 채우기
const fetchReviewDetails = async (reviewId) => {
    try {
        const response = await axios.get(`https://43.201.83.17/api/v1/evaluations/review/${reviewId}/`, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('access')}`
            }
        });
        const review = response.data;
        // 폼에 기존 리뷰 내용과 평점 채우기
        document.getElementById("edit-review-content").value = review.content;
        document.getElementById("edit-review-rating").value = review.rating;

    } catch (error) {
        alert('리뷰를 불러오지못했습니다. 다시시도해주세요.');
    }
};

// 리뷰 수정 요청 처리
document.getElementById("edit-review-form").addEventListener("submit", async function(event) {
    event.preventDefault();  // 폼 제출 동작 막기

    const reviewId = new URLSearchParams(window.location.search).get('reviewId');  // URL에서 reviewId 가져오기
    const newContent = document.getElementById("edit-review-content").value;
    const newRating = document.getElementById("edit-review-rating").value;

    try {
        const response = await axios.put(`https://43.201.83.17/api/v1/evaluations/review/${reviewId}/`, {
            content: newContent,
            rating: newRating
        }, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('access')}`,
                'Content-Type': 'application/json'
            }
        });
         // 응답 데이터 확인
        if (response.status === 200) {
            alert('수정이 완료되었습니다!');
            window.location.href = document.referrer;
        }
    } catch (error) {
        alert('수정실패 다시시도해주세요.');
    }
});

// DOM 로드 후 기존 리뷰 데이터 불러오기
document.addEventListener('DOMContentLoaded', () => {
    const reviewId = new URLSearchParams(window.location.search).get('reviewId');
    fetchReviewDetails(reviewId);
});
