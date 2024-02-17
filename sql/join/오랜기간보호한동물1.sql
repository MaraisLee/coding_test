-- [문제] https://school.programmers.co.kr/learn/courses/30/lessons/59044

SELECT A.NAME, A.DATETIME -- 보여줄 열 목록
FROM ANIMAL_INS A -- 첫번째 테이블
LEFT JOIN ANIMAL_OUTS B -- (첫번째 테이블에만 해당하는 것 찾을 때), 두번째테이블 
ON A.ANIMAL_ID = B.ANIMAL_ID -- 조인 조건
WHERE B.ANIMAL_ID IS NULL -- 검색 조건, 조인했으므로 두번째 테이블에는 남아있지 않음
ORDER BY A.DATETIME --정렬기준
LIMIT 3 -- 개수 제한