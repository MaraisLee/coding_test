-- [문제] https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B
INNER JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID -- 조인 조건
WHERE B.CATEGORY = '경제' -- 검색 조건
ORDER BY B.PUBLISHED_DATE -- 기본값이 오름차순