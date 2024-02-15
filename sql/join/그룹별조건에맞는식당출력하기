-- https://school.programmers.co.kr/learn/courses/30/lessons/131124

SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') -- 코드실행시 날짜 포맷 꼭 확인해보기 
FROM MEMBER_PROFILE P
JOIN REST_REVIEW R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(*) DESC -- 개수로 내림차순
    LIMIT 1 -- 그중 젤 위, 즉 젤 높은 숫자 
)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT