-- 코드를 입력하세요
# SELECT a.BOOK_ID, b.AUTHOR_NAME, DATE_FORMAT(a.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
# FROM BOOK AS a
# JOIN AUTHOR AS b
# ON a.AUTHOR_ID = b.AUTHOR_ID
# WHERE a.CATEGORY = '경제'
# ORDER BY a.PUBLISHED_DATE

SELECT 
    b.book_id, 
    a.author_name, 
    DATE_FORMAT(b.published_date, '%Y-%m-%d') AS published_date
FROM book AS b
    JOIN author AS a
    ON b.author_id = a.author_id
WHERE b.category = '경제'
ORDER BY published_date