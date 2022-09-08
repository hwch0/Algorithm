-- 코드를 입력하세요
SELECT ins.name, ins.datetime
FROM animal_ins ins
LEFT OUTER JOIN animal_outs outs ON ins.animal_id = outs.animal_id
where outs.datetime is null
ORDER BY ins.datetime
LIMIT 3