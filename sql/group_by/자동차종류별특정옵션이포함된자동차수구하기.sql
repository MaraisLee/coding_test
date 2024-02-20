-- https://school.programmers.co.kr/learn/courses/30/lessons/151137

SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%시트%' -- WHERE A LIKE '%특정문자열%' --  특정문자열을 포함하는 값
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE