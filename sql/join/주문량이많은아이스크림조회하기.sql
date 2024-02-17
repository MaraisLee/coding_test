-- https://school.programmers.co.kr/learn/courses/30/lessons/133027

SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN JULY J
ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR -- 나오는 결과 테이블의 기준
ORDER BY (SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER)) DESC -- 각 테이블에서 합을 더해서(같은 맛이라도 shipement_id가 다를 수 있기 때문), 전체를 더하기 
LIMIT 3