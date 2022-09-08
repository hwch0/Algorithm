-- 코드를 입력하세요
select cart.cart_id
FROM 
(SELECT cart_id
, count(if(name='Yogurt', 1, null)) Yogurt
, count(if(name='Milk', 1, null)) Milk
FROM cart_products
GROUP BY cart_id
HAVING Yogurt>0 and Milk>0) cart