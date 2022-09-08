-- 코드를 입력하세요
SELECT ins.animal_id, ins.name
FROM animal_ins ins
INNER JOIN animal_outs outs on ins.animal_id = outs.animal_id 
    and ins.datetime > outs.datetime
ORDER BY ins.datetime