-- https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL -- 이름이 없는 동물은 집계에서 제외
GROUP BY NAME
HAVING COUNT > 1 -- 두 번 이상 쓰인 이름 
ORDER BY NAME