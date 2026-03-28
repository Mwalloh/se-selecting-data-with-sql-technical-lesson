import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')


""" Quick note on string syntax """
employee_data = pd.read_sql(""" 
    SELECT * 
    FROM employees; 
""", conn)

print(employee_data)


""" Retrieving a subset of columns """
employees_first_and_last = pd.read_sql(""" 
    SELECT firstName, lastName 
    FROM employees; 
""", conn).head()

print(employees_first_and_last)


""" Retrieving columns as Aliases """
employees_first_names = pd.read_sql(""" 
    SELECT firstName AS name
    FROM employees; 
""", conn).head()

print(employees_first_names)


""" CASE to Bin column values """
employees_by_role = pd.read_sql(""" 
    SELECT firstName, lastName, jobTitle,
        CASE 
        WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
        ELSE "Not Sales Rep"
        END AS role         
    FROM employees; 
""", conn).head(10)

print(employees_by_role)


""" CASE to make values human-readable """
employees_with_location = pd.read_sql(""" 
    SELECT firstName, lastName, officeCode,
        CASE 
        WHEN officeCode = "1" THEN "San Francisco, CA"
        WHEN officeCode = "2" THEN "Boston, MA"
        WHEN officeCode = "3" THEN "New York, NY"
        WHEN officeCode = "4" THEN "Paris, France"
        WHEN officeCode = "5" THEN "Tokyo, Japan"
        END AS office
    FROM employees; 
""", conn).head(10)

print(employees_with_location)


""" Built-in SQL functions for string manipulations """
employee_name_lengths = pd.read_sql(""" 
    SELECT length(firstName) AS name_length
    FROM employees; 
""", conn).head()

print(employee_name_lengths)

upper_employees = pd.read_sql(""" 
    SELECT upper(firstName) AS name_in_all_caps
    FROM employees; 
""", conn).head()

print(upper_employees)

employee_initials = pd.read_sql(""" 
    SELECT substr(firstName, 1, 1) || "." AS first_initial
    FROM employees; 
""", conn).head()

print(employee_initials)

employee_full_names = pd.read_sql("""
    SELECT firstName || " " || lastName AS full_name
    FROM employees;                 
""", conn).head()

print(employee_full_names)


""" Built-in SQL functions for Math operations """
order_details = pd.read_sql(""" 
    SELECT * 
    FROM orderDetails; 
""", conn)

print(order_details)

rounded_prices = pd.read_sql(""" 
    SELECT round(priceEach) AS rounded_price
    FROM orderDetails; 
""", conn)

print(rounded_prices)

rounded_prices_int = pd.read_sql(""" 
    SELECT CAST(round(priceEach) AS INTEGER) AS rounded_price_int
    FROM orderDetails; 
""", conn)

print(rounded_prices_int)


""" Basic Math operations """
totals = pd.read_sql(""" 
    SELECT priceEach * quantityOrdered AS total_price
    FROM orderDetails; 
""", conn)

print(totals)


""" Built-in SQL functions for Date and Time operations """
orders = pd.read_sql(""" 
    SELECT * 
    FROM orders; 
""", conn)

print(orders)

days_remaining = pd.read_sql(""" 
    SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
    FROM orders; 
""", conn)

print(days_remaining)

order_dates = pd.read_sql("""
    SELECT orderDate, date(orderDate, "+7 days") AS one_week_later
    FROM orders;
""", conn)

print(order_dates)

order_dates = pd.read_sql("""
    SELECT orderDate,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year,
       strftime("%d", orderDate) AS day
    FROM orders;
""", conn)

print(order_dates)

conn.close()