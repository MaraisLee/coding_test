-- https://school.programmers.co.kr/learn/courses/30/lessons/144856

SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(S.SALES* B.PRICE) AS TOTAL_SALES
FROM BOOK B
JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES S
ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE LIKE '2022-01%' -- 도서 판매 데이터를 기준으로
GROUP BY B.AUTHOR_ID, B.CATEGORY --  저자 별, 카테고리 별
ORDER BY B.AUTHOR_ID, B.CATEGORY DESC