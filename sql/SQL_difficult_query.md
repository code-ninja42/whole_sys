Q3 — Hard

Display products ordered first by category_id ascending, and within each category, by price descending.


USE ecommerce_db;

SELECT * from products
order by category_id desc, price asc;

Q3 — Hard

Display product_name, price, and calculate the profit per unit as:

price - cost_price

Give the calculated column the name profit.
SELECT product_name,price,
price -cost_price as profit 
from products;

Q3 — Hard

Display the 3rd, 4th, and 5th most expensive products.
with rank_range as (
    SELECT *,
    dense_rank() over(
        order by price DESC
        ) as dense_rank_num 
   from products
    )
    SELECT * from rank_range
    where dense_rank_num in(3,4,5);

CTE - QUE 
Create a CTE containing products with price > 5000, then display them.

with price_greater as(
select * 
from products

Create a CTE that calculates total quantity sold for each product, then display products whose quantity sold is greater than 2
WITH total_quant AS (
    SELECT product_id, SUM(quantity) AS total_quantity
    FROM order_items
    GROUP BY product_id
)
SELECT *
FROM total_quant
WHERE total_quantity > 2;



Row_number()
1.Assign a row number to every product ordered by price descending

SELECT *,
row_number() over(
    
    order by price DESC
    ) as row_num
from products;

2.
Find the highest-priced product from each category using ROW_NUMBER().
with ranked_category AS (
    SELECT *, 
    row_number() over(
        PARTITION by category_id
        order by price DESC
        ) as row_num 
    from products
   )
SELECT * from ranked_category 
    WHERE row_num = 1;


Rank()
Rank all products based on price from highest to lowest.
SELECT *,
rank() over(
    order by price DESC
    )as rank_num
  from products;



Dense_rank()
Find the second-highest distinct price in each category using DENSE_RANK().
with second_highest as (
    SELECT *,
    dense_rank() over(
        
        order by cost_price desc
        ) as dense_rank_num
    from products
    )
SELECT * from second_highest 
WHERE dense_rank_num = 2;
   


Previous row ← LAG | Current row | LEAD → Next row
SELECT product_name, price,
       LEAD(price) OVER (
           ORDER BY price
       ) AS next_price
FROM products;

SELECT product_name, price,
       LAG(price) OVER (
           ORDER BY price
       ) AS previous_price
FROM products;
