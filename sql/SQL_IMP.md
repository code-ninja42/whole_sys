# SQL-Based E-Commerce Analytics Project

## For Data Analytics (DA) , Data Science (DS) & PYTHON Students

---

## 1. Project Title

**E-Commerce Sales & Customer Analytics System**

---

## 2. Project Objective

Build a complete SQL-based data analytics project using an **E-Commerce database**.

Students will work with customer, product, order, payment, delivery, and review data.

The goal is to use SQL to answer real-world business questions and generate useful insights.

---

## 3. Business Scenario

You are working as a **Data Analyst** for an e-commerce company.

The management team wants to understand:

* Which products generate the most revenue?
* Which customers are most valuable?
* Which product categories perform well?
* What are the monthly sales trends?
* Which cities generate the highest sales?
* What percentage of orders are cancelled?
* What is the average order value?
* Which customers have not purchased recently?
* Which products have low stock?
* How does delivery performance vary?
* Which products have the best customer ratings?

Your task is to analyze the company's database using SQL and prepare meaningful business insights.

---

# 4. Database Structure

Create the following tables:

```text
customers
    │
    ├──────── orders
    │             │
    │             ├──── order_items ──── products
    │             │                         │
    │             │                         └──── categories
    │             │
    │             └──── payments
    │
    └──── reviews

orders ─── deliveries
```

---

# 5. Tables

## 5.1 Customers

Stores customer information.

| Column            | Data Type | Description       |
| ----------------- | --------- | ----------------- |
| customer_id       | INT       | Primary Key       |
| customer_name     | VARCHAR   | Customer name     |
| email             | VARCHAR   | Customer email    |
| gender            | VARCHAR   | Male/Female/Other |
| age               | INT       | Customer age      |
| city              | VARCHAR   | Customer city     |
| state             | VARCHAR   | Customer state    |
| registration_date | DATE      | Registration date |

---

## 5.2 Categories

Stores product categories.

| Column        | Data Type | Description   |
| ------------- | --------- | ------------- |
| category_id   | INT       | Primary Key   |
| category_name | VARCHAR   | Category name |

Example categories:

```text
Electronics
Fashion
Home & Kitchen
Beauty
Sports
Books
Grocery
Toys
Furniture
Accessories
```

---

## 5.3 Products

Stores product information.

| Column         | Data Type | Description     |
| -------------- | --------- | --------------- |
| product_id     | INT       | Primary Key     |
| product_name   | VARCHAR   | Product name    |
| category_id    | INT       | Foreign Key     |
| price          | DECIMAL   | Selling price   |
| cost_price     | DECIMAL   | Product cost    |
| stock_quantity | INT       | Available stock |

---

## 5.4 Orders

Stores order information.

| Column        | Data Type | Description   |
| ------------- | --------- | ------------- |
| order_id      | INT       | Primary Key   |
| customer_id   | INT       | Foreign Key   |
| order_date    | DATE      | Order date    |
| order_status  | VARCHAR   | Order status  |
| shipping_city | VARCHAR   | Delivery city |

Possible order statuses:

```text
Pending
Confirmed
Shipped
Delivered
Cancelled
Returned
```

---

## 5.5 Order Items

Stores products purchased in each order.

| Column        | Data Type | Description        |
| ------------- | --------- | ------------------ |
| order_item_id | INT       | Primary Key        |
| order_id      | INT       | Foreign Key        |
| product_id    | INT       | Foreign Key        |
| quantity      | INT       | Quantity purchased |
| unit_price    | DECIMAL   | Selling price      |
| discount      | DECIMAL   | Discount amount    |

---

## 5.6 Payments

Stores payment information.

| Column         | Data Type | Description    |
| -------------- | --------- | -------------- |
| payment_id     | INT       | Primary Key    |
| order_id       | INT       | Foreign Key    |
| payment_date   | DATE      | Payment date   |
| payment_method | VARCHAR   | Payment method |
| payment_status | VARCHAR   | Payment status |
| amount         | DECIMAL   | Payment amount |

Payment methods:

```text
UPI
Credit Card
Debit Card
Cash on Delivery
Net Banking
Wallet
```

---

## 5.7 Deliveries

Stores delivery information.

| Column           | Data Type | Description      |
| ---------------- | --------- | ---------------- |
| delivery_id      | INT       | Primary Key      |
| order_id         | INT       | Foreign Key      |
| shipped_date     | DATE      | Shipping date    |
| delivered_date   | DATE      | Delivery date    |
| delivery_status  | VARCHAR   | Delivery status  |
| delivery_partner | VARCHAR   | Delivery partner |

---

## 5.8 Reviews

Stores customer product reviews.

| Column      | Data Type | Description        |
| ----------- | --------- | ------------------ |
| review_id   | INT       | Primary Key        |
| customer_id | INT       | Foreign Key        |
| product_id  | INT       | Foreign Key        |
| rating      | INT       | Rating from 1 to 5 |
| review_date | DATE      | Review date        |
| review_text | TEXT      | Customer review    |

Rating:

```text
1 = Very Bad
2 = Bad
3 = Average
4 = Good
5 = Excellent
```

---

# 6. SQL Concepts Students Must Practice

## Basic SQL

* SELECT
* WHERE
* ORDER BY
* DISTINCT
* LIMIT
* BETWEEN
* IN
* LIKE

## Aggregate Functions

* COUNT()
* SUM()
* AVG()
* MIN()
* MAX()

## Grouping

* GROUP BY
* HAVING

## Joins

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* Multiple-table JOIN

## Conditional Logic

* CASE

## Subqueries

* Scalar subqueries
* Correlated subqueries
* Subqueries with IN
* Subqueries with EXISTS

## CTE

* WITH
* Multiple CTEs

## Window Functions

* ROW_NUMBER()
* RANK()
* DENSE_RANK()
* LAG()
* LEAD()
* SUM() OVER()

## Database Concepts

* Primary Key
* Foreign Key
* Constraints
* Normalization
* Indexing
* Views

---

# 7. Project Tasks

# LEVEL 1 — BASIC SQL

## Task 1

Display all customers.

---

## Task 2

Find all customers from Ahmedabad.

---

## Task 3

Find customers whose age is greater than 30.

---

## Task 4

Display all unique customer cities.

---

## Task 5

Find products costing more than ₹10,000.

---

## Task 6

Display all delivered orders.

---

## Task 7

Find products belonging to the Electronics category.

---

## Task 8

Find customers whose name starts with the letter `A`.

---

## Task 9

Find customers whose age is between 20 and 30.

---

## Task 10

Find all orders placed between two specific dates.

---

# LEVEL 2 — AGGREGATION

## Task 11

Find the total number of customers.

Expected output:

```text
Total Customers
```

---

## Task 12

Find the total number of orders.

---

## Task 13

Calculate total revenue.

---

## Task 14

Calculate the average order value.

---

## Task 15

Find the minimum product price.

---

## Task 16

Find the maximum product price.

---

## Task 17

Find the number of customers in each city.
SELECT city,count(*) as total_count 
from customers
GROUP by city ;
Expected output:

```text
City
Customer Count
```

---

## Task 18

Find the number of orders for each order status.
SELECT order_status,count(*) as total_count 
from orders
GROUP by order_status
order by total_count DESC;
Expected output:

```text
Order Status
Order Count
```

---

## Task 19

Find total revenue by city.

---

## Task 20

Find total revenue by product category.

---

# LEVEL 3 — JOIN ANALYSIS

## Task 21

Display:

```text
Customer Name
Order ID
Order Date
Order Status
```

Use:

```text
customers
orders
```

---

## Task 22

Display:

```text
Product Name
Category Name
Price
Stock Quantity
```

Use:

```text
products
categories
```

SELECT p.product_name,c.category_name,p.price,p.stock_quantity
from products as p 
join categories as c 
on c.category_id = p.category_id;

---

## Task 23

Display:

```text
Customer Name
Order ID
Product Name
Quantity
Unit Price
```

Use:

```text
customers
orders
order_items
products
```
SELECT 
    c.customer_name,
    o.order_id,
    p.product_name,
    oi.quantity,
    oi.unit_price
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
JOIN order_items AS oi
    ON o.order_id = oi.order_id
JOIN products AS p
    ON oi.product_id = p.product_id;

---

## Task 24

Find total spending for each customer.

Expected output:

```text
Customer Name
Total Spending
```

---

## Task 25

Find total quantity sold for each product.

Expected output:

```text
Product Name
Total Quantity Sold
```

---

## Task 26

Find total revenue generated by each product.

---

## Task 27

Find revenue generated by each category.

---

## Task 28

Find the number of orders placed by each customer.

---

# LEVEL 4 — BUSINESS ANALYSIS

## Task 29 — Top Customers

Find the top 10 customers based on total spending.

Expected output:

```text
Customer
Total Spending
```

---

## Task 30 — Best-Selling Products

Find the top 10 products based on quantity sold.

---

## Task 31 — Revenue Leaders

Find the top 10 products based on revenue.

---

## Task 32 — Category Performance

Calculate:

```text
Category
Total Orders
Total Quantity Sold
Total Revenue
Average Selling Price
```

---

## Task 33 — City Performance

Calculate:

```text
City
Customers
Orders
Revenue
Average Order Value
```

---

## Task 34 — Payment Analysis

Find the number of transactions and total amount for each payment method.

Expected output:

```text
Payment Method
Transactions
Total Amount
```

---

## Task 35 — Order Status Analysis

Calculate the percentage of orders belonging to each order status.

---

# LEVEL 5 — CUSTOMER ANALYTICS

## Task 36 — Repeat Customers

Find customers who have placed more than one order
select customer_id,count(*) as total_count 
from customers
group by customer_id
having count(*) > 1;

---

## Task 37 — One-Time Customers

Find customers who have placed exactly one order.

just
having count(*) = 1;
---

## Task 38 — Inactive Customers

Find customers who registered but have never placed an order.

---

## Task 39 — Recent Customers

Find customers who registered within the last 6 months.

---

## Task 40 — Highest Spending Customer

Find the customer with the highest total spending.

---

## Task 41 — Average Customer Spending

Calculate the average amount spent per customer.

---

## Task 42 — Customer Segmentation

Create customer segments using `CASE`.

Use the following rules:

```text
0 – 10,000
Low Value

10,001 – 50,000
Medium Value

50,001+
High Value
```

Expected output:

```text
Customer
Total Spending
Customer Segment
```

---

# LEVEL 6 — TIME-SERIES ANALYSIS

## Task 43 — Monthly Revenue

Calculate monthly revenue.

Expected output:

```text
Month
Revenue
```

---

## Task 44 — Monthly Orders

Calculate the number of orders for each month.

---

## Task 45 — Yearly Revenue

Calculate yearly revenue.

---

## Task 46 — Best Sales Month

Find the month with the highest revenue.

---

## Task 47 — Monthly Average Order Value

Calculate the average order value for every month.

---

## Task 48 — Monthly Growth

Calculate:

```text
Month
Current Month Revenue
Previous Month Revenue
Growth %
```

Use:

```sql
LAG()
```

---

# LEVEL 7 — PRODUCT ANALYTICS

## Task 49 — Low Stock Products

Find products where stock quantity is less than 10.

---

## Task 50 — Out-of-Stock Products

Find products where stock quantity is 0.

---

## Task 51 — Unsold Products

Find products that have never been ordered.

---

## Task 52 — Product Profit

Calculate:

```text
Profit = Selling Price - Cost Price
```

Find the products with the highest profit per unit.

---

## Task 53 — Total Product Profit

Calculate total profit generated by each product.

---

## Task 54 — Category Profit

Calculate total profit for each category.

---

## Task 55 — Product Ranking

Rank products within each category according to revenue.

Use:

```sql
RANK()
```

Expected output:

```text
Category
Product
Revenue
Rank
```

---

## Task 56 — Top Product Per Category

Find the highest-revenue product from every category.

---

# LEVEL 8 — REVIEW ANALYTICS

## Task 57

Calculate the average rating for every product.

---

## Task 58

Find products with an average rating greater than 4.

---

## Task 59

Find the highest-rated products.

---

## Task 60

Find the lowest-rated products.

---

## Task 61

Calculate average rating by category.

---

## Task 62

Find the number of reviews received by each product.

---

## Task 63

Find products that have more than 100 reviews.

---

## Task 64

Find customers who have given an average rating below 3.

---

# LEVEL 9 — DELIVERY ANALYTICS

## Task 65 — Delivery Time

Calculate the number of days taken for each delivery.

Formula:

```text
Delivery Days =
Delivered Date - Shipped Date
```

---

## Task 66 — Delayed Orders

Find orders that took more than 5 days to deliver.

---

## Task 67 — Delivery Partner Performance

Calculate:

```text
Delivery Partner
Total Deliveries
Average Delivery Days
Delayed Orders
```

---

## Task 68 — Delivery Status

Find the number of orders for each delivery status.

---

## Task 69 — Cancellation Rate

Calculate the percentage of cancelled orders.

Formula:

```text
Cancellation Rate =
Cancelled Orders / Total Orders × 100
```

---

# LEVEL 10 — ADVANCED SQL

## Task 70 — Customer Ranking

Rank customers according to total spending.

Expected output:

```text
Customer
Total Spending
Rank
```

Use:

```sql
DENSE_RANK()
```

---

## Task 71 — Running Revenue

Calculate cumulative monthly revenue.

Use:

```sql
SUM() OVER(...)
```

Expected output:

```text
Month
Monthly Revenue
Cumulative Revenue
```

---

## Task 72 — Previous Purchase

For every customer, display:

```text
Customer
Order Date
Previous Order Date
```

Use:

```sql
LAG()
```

---

## Task 73 — Next Purchase

For every customer, display:

```text
Customer
Order Date
Next Order Date
```

Use:

```sql
LEAD()
```

---

## Task 74 — Purchase Gap

Calculate the number of days between consecutive purchases of each customer.

---

## Task 75 — Customer First Purchase

Find the first order date of every customer.

---

## Task 76 — Customer Latest Purchase

Find the most recent order date of every customer.

---

## Task 77 — Top 3 Products Per Category

Find the top 3 products based on revenue within every category.
WITH product_revenue AS (
    SELECT
        category_id,
        product_id,
        product_name,
        SUM(price * stock_quantity) AS revenue
    FROM products
    GROUP BY category_id, product_id, product_name
),

ranked_products AS (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY category_id
               ORDER BY revenue DESC
           ) AS rnk
    FROM product_revenue
)

SELECT
    category_id,
    product_id,
    product_name,
    revenue
FROM ranked_products
WHERE rnk <= 3
ORDER BY category_id, revenue DESC;

Use:

```sql
ROW_NUMBER()
```

or

```sql
DENSE_RANK()
```

---

# LEVEL 11 — CTE PRACTICE

## Task 78

Create a CTE that calculates total spending per customer.

Then use the CTE to find customers whose spending is above ₹50,000.
with  total_spending as (
    SELECT category_id, sum(price) as total_amount
    from products 
    GROUP by category_id
    )
    
    SELECT * from total_spending 
    where total_amount > 5000;
---

## Task 79

Create a CTE for monthly revenue.

Then calculate the average monthly revenue.

---

## Task 80

Create a CTE for product revenue.

Then find products whose revenue is greater than the average product revenue.
with  total_spending as (
    SELECT *, avg(price) as avg_amount
    from products 
    
    )
    
    SELECT * from total_spending 
    where price > avg_amount;
---

# LEVEL 12 — SUBQUERY PRACTICE

## Task 81

Find products whose price is greater than the average product price.
SELECT * FROM products where price > (SELECT avg(price) as avg_product from products);

---

## Task 82

Find customers whose total spending is greater than the average customer spending.

---

## Task 83

Find products that belong to the category having the highest average product price.

---

## Task 84

Find customers who have placed an order but have never given a review.

---

# LEVEL 13 — SQL VIEW

Create a view named:

```text
customer_sales_summary
```

The view should contain:

```text
customer_id
customer_name
city
total_orders
total_quantity
total_spending
average_order_value
last_order_date
```

Example:

```sql
CREATE VIEW customer_sales_summary AS
SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COALESCE(SUM(oi.quantity), 0) AS total_quantity,
    COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total_spending,
    COALESCE(AVG(oi.quantity * oi.unit_price), 0) AS average_order_value,
    MAX(o.order_date) AS last_order_date
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
LEFT JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_name,
    c.city;
```

---

# LEVEL 14 — DATA SCIENCE EXTENSION

## RFM Customer Analysis

For Data Science students, perform RFM analysis.

RFM stands for:

```text
R = Recency
F = Frequency
M = Monetary
```

---

## Recency

Calculate how recently each customer purchased.

Formula:

```text
Recency =
Current Date - Last Order Date
```

---

## Frequency

Calculate how frequently the customer purchased.

```text
Frequency =
Number of Orders
```

---

## Monetary

Calculate how much money the customer spent.

```text
Monetary =
Total Spending
```

---

## Final RFM Dataset

Create:

```text
customer_id
customer_name
recency
frequency
monetary
```

Then assign scores from 1 to 5.

Final output:

```text
Customer
Recency Score
Frequency Score
Monetary Score
RFM Score
```

Example segments:

```text
High Value Customer
Loyal Customer
Potential Customer
At Risk Customer
Inactive Customer
```

---

# 15. Dashboard Requirements

After completing the SQL analysis, connect the database to a visualization tool.

Recommended tools:

* Power BI
* Tableau
* Excel
* Python

---

# 16. Dashboard KPIs

The dashboard should contain:

```text
Total Revenue
Total Orders
Total Customers
Average Order Value
Total Products
Cancellation Rate
Average Rating
Average Delivery Time
```

---

# 17. Dashboard Charts

Create the following visualizations:

### Chart 1

Monthly Revenue Trend

### Chart 2

Revenue by Category

### Chart 3

Top 10 Products by Revenue

### Chart 4

Top 10 Customers by Spending

### Chart 5

Revenue by City

### Chart 6

Customer Segmentation

### Chart 7

Payment Method Distribution

### Chart 8

Order Status Distribution

### Chart 9

Delivery Partner Performance

### Chart 10

Product Rating Analysis

---

# 18. Suggested Dashboard Layout

```text
+-------------------------------------------------------+
|              E-COMMERCE ANALYTICS                    |
+-------------------------------------------------------+

| Revenue | Orders | Customers | AOV | Cancellation % |
|-------------------------------------------------------|

|              Monthly Revenue Trend                   |
|                                                       |
+-------------------------------------------------------+

| Revenue by Category | Revenue by City                  |
|                      |                                  |
+----------------------+----------------------------------+

| Top Products         | Customer Segments                |
|                      |                                  |
+----------------------+----------------------------------+

| Payment Methods      | Order Status                     |
|                      |                                  |
+----------------------+----------------------------------+
```

---

# 19. Recommended Dataset Size

For classroom practice, use a reasonably large dataset.

| Table       | Recommended Records |
| ----------- | ------------------: |
| Customers   |               5,000 |
| Categories  |                  10 |
| Products    |                 500 |
| Orders      |              20,000 |
| Order Items |             40,000+ |
| Payments    |              20,000 |
| Deliveries  |              20,000 |
| Reviews     |             15,000+ |

The objective is to give students enough data to practice real analytical queries instead of working with only a few sample records.

---

# 20. Final Deliverables

Students must submit the following:

## 1. Database SQL File

```text
ecommerce.sql
```

Should contain:

* CREATE TABLE
* Primary Keys
* Foreign Keys
* Constraints
* INSERT statements
* Indexes
* Views

---

## 2. Analysis SQL File

```text
analysis.sql
```

Should contain all analytical queries.

---

## 3. Dashboard

```text
E-Commerce Analytics Dashboard
```

---

## 4. Project Report

The report should contain:

```text
1. Project Introduction
2. Business Problem
3. Project Objective
4. Database Design
5. ER Diagram
6. Table Descriptions
7. SQL Queries
8. Analysis
9. Key Findings
10. Dashboard Screenshots
11. Business Insights
12. Conclusion
```

---

# 21. Final Project Challenge

## Business Problem

> The management team wants to understand sales performance, customer behavior, product performance, payment patterns, reviews, and delivery performance.

Using the available database, perform a complete analysis and answer:

### Sales

* How much revenue is generated?
* What are the monthly sales trends?
* Which categories generate the most revenue?
* Which cities generate the most revenue?

### Customers

* Who are the highest-spending customers?
* How many repeat customers are there?
* How many one-time customers are there?
* Which customers are inactive?
* What are the different customer segments?

### Products

* Which products sell the most?
* Which products generate the most revenue?
* Which products generate the most profit?
* Which products have low stock?
* Which products are never sold?

### Payments

* Which payment method is used most frequently?
* Which payment method generates the highest transaction value?
* What is the payment success/failure pattern?

### Reviews

* Which products have the highest ratings?
* Which products have poor ratings?
* Which categories receive better ratings?

### Delivery

* What is the average delivery time?
* Which delivery partners have delayed deliveries?
* What percentage of orders are cancelled?

---

# 22. Final Data Science Challenge

Use SQL to prepare a customer-level dataset containing:

```text
customer_id
total_orders
total_spending
average_order_value
last_order_date
days_since_last_order
total_products_purchased
average_rating_given
preferred_payment_method
city
```

Then export the dataset and use Python to perform:

```text
1. Exploratory Data Analysis
2. Customer Segmentation
3. RFM Analysis
4. Visualization
5. Correlation Analysis
6. Feature Engineering
7. Customer Churn Analysis
```

Optional advanced extensions:

```text
Customer Churn Prediction
Sales Forecasting
Product Recommendation
Customer Lifetime Value
```

---

# 23. Project Workflow

```text
                    E-COMMERCE PROJECT
                           │
                           ▼
                   Database Design
                           │
                           ▼
                    Create Tables
                           │
                           ▼
                     Insert Data
                           │
                           ▼
                    Basic SQL
                           │
                           ▼
                    Aggregations
                           │
                           ▼
                        JOINs
                           │
                           ▼
                 Business Questions
                           │
                           ▼
                    Advanced SQL
                           │
                           ▼
                    RFM Analysis
                           │
                           ▼
                       Python
                           │
                           ▼
                      Dashboard
                           │
                           ▼
                  Business Insights
```

---

# 24. Learning Outcomes

After completing this project, students should be able to:

* Design a relational database.
* Understand primary and foreign keys.
* Write SQL queries.
* Filter and sort data.
* Perform aggregation.
* Work with multiple tables using JOINs.
* Solve real-world business problems using SQL.
* Use subqueries and CTEs.
* Use window functions.
* Perform customer analytics.
* Perform product analytics.
* Perform time-series analysis.
* Perform RFM analysis.
* Prepare datasets for Data Science.
* Build an analytical dashboard.
* Present data-driven business insights.

---

# 25. Difficulty Progression

```text
LEVEL 1
Basic SELECT / WHERE
        ↓
LEVEL 2
GROUP BY / Aggregations
        ↓
LEVEL 3
JOINs
        ↓
LEVEL 4
Business Analysis
        ↓
LEVEL 5
Customer Analytics
        ↓
LEVEL 6
Time-Series Analysis
        ↓
LEVEL 7
Product Analytics
        ↓
LEVEL 8
Review & Delivery Analytics
        ↓
LEVEL 9
Advanced SQL
        ↓
LEVEL 10
CTEs / Subqueries / Window Functions
        ↓
LEVEL 11
RFM Analysis
        ↓
LEVEL 12
Python + Dashboard
```

---

# 26. Important Student Rule

Students should **not directly search for the SQL query for every question**.

First follow this process:

1. Understand the business question
2. Identify required tables
3. Identify required columns
4. Decide whether JOIN is required
5. Decide whether GROUP BY is required
6. Decide whether aggregation is required
7. Write the SQL query
8. Execute the query
9. Validate the result
10. Explain the business insight
