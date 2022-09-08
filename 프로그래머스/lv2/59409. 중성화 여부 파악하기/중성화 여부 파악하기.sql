-- 코드를 입력하세요
SELECT animal_id, name,
if(sex_upon_intake like 'Intact%', 'X', 'O')
FROM animal_ins