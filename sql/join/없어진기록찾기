-- https://school.programmers.co.kr/learn/courses/30/lessons/59042

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I
RIGHT JOIN ANIMAL_OUTS O -- 다이어그램을 가정했을 때, 왼쪽 테이블에는 없고 오른쪽엔 있는 경우 (다이어그램 그리면서 join 종류 구별하기)
ON I.ANIMAL_ID = O.ANIMAL_ID -- ID를 조인하려고하는데
WHERE I.ANIMAL_ID IS NULL -- 값이 없는 경우 NULL로 채워짐 
ORDER BY O.ANIMAL_ID
