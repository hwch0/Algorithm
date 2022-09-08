-- 코드를 입력하세요
SELECT animal_type
    , if (name is not null, name, 'No name') NAME
    , sex_upon_intake
FROM animal_ins
ORDER BY animal_id