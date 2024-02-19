-- https://school.programmers.co.kr/learn/courses/30/lessons/59413

SET @HOUR = -1; -- 변수로 설정
SELECT (@HOUR := @HOUR + 1) AS HOUR, -- 1번째 열 (변수에 1씩 더하면서 0-23h을 만듦)
    (SELECT COUNT(HOUR(DATETIME)) -- 2번째 열
    FROM ANIMAL_OUTS          
    WHERE HOUR(DATETIME) = @HOUR) AS COUNT -- 변수랑 맞는 HOUR(DATETIME)의 수를 count
FROM ANIMAL_OUTS
WHERE @HOUR < 23; -- 23h 이하,  변수에 22번 1을 더하라는 의미 (-1부터 시작했으니 23이되려면 22번만 더하면 됨)