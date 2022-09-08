-- 코드를 입력하세요
SELECT ins.animal_id, ins.animal_type, ins.name
FROM animal_ins ins
INNER JOIN animal_outs outs ON ins.animal_id = outs.animal_id
WHERE ins.SEX_UPON_INTAKE like 'Intact%'
AND outs.SEX_UPON_OUTCOME not like 'Intact%'
ORDER BY ins.animal_id