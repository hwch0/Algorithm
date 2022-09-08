-- 코드를 입력하세요
SELECT p1.id, p1.name, p1.host_id
FROM places p1
INNER JOIN 
(SELECT host_id, count(*) cnt
FROM places
GROUP BY host_id
HAVING cnt >= 2) p2 ON p1.host_id = p2.host_id

ORDER BY p1.id