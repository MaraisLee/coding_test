-- https://school.programmers.co.kr/learn/courses/30/lessons/164668

SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE' 
GROUP BY B.WRITER_ID
HAVING TOTAL_SALES	>= 700000 -- 연산한 함수의 별칭을 기준으로 정렬할 경우 그 조건은 having절에. 
ORDER BY TOTAL_SALES