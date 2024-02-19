-- https://school.programmers.co.kr/learn/courses/30/lessons/131123

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) 
                                FROM REST_INFO
                                GROUP BY FOOD_TYPE)
                                -- FOOD_TYPE에 따른 가장 FAVORITES이 높은 값을 불러옴
ORDER BY FOOD_TYPE DESC