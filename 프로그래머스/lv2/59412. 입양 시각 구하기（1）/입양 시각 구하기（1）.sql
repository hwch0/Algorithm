-- 코드를 입력하세요
SELECT hour(datetime) hour, count(*)
FROM animal_outs
GROUP BY hour
HAVING hour>=9 and hour <=19
ORDER BY hour