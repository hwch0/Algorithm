-- 코드를 입력하세요
SELECT sub.id, sub.name
FROM 
(SELECT ins.animal_id id, ins.name name
, datediff(outs.datetime, ins.datetime) date
FROM animal_ins ins
INNER JOIN animal_outs outs ON ins.animal_id = outs.animal_id 
ORDER BY date desc
LIMIT 2) sub