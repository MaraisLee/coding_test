-- https://school.programmers.co.kr/learn/courses/30/lessons/131532

SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH, U.GENDER, COUNT(DISTINCT U.USER_ID) AS USERS -- 중복된 값들중 하나씩만 계산하고 싶을 때!
FROM USER_INFO U
JOIN ONLINE_SALE O
ON U.USER_ID = O.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY MONTH(O.SALES_DATE), U.GENDER -- 달별, 성별로 구분되어있음 
ORDER BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), U.GENDER