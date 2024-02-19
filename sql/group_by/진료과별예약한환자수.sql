-- https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = '2022' AND MONTH(APNT_YMD) = '05'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, MCDP_CD -- GROUP BY, ORDER BY, HAVING절에 별칭을 쓸 경우 별칭 그대로 쓰거나, 백틱사용!