# Mastering SQL: A Step-by-Step Guide

## Day 1: Mastering the SELECT Statement - Your Key to Data Retrieval 🔑

[Watch Video](https://youtu.be/HYD8KjPB9F8)

Welcome back, data enthusiasts! 📊 In this lesson, we'll explore the powerful `SELECT` statement, your gateway to extracting valuable insights from your database. Let's dive in! 🚀

### Understanding the SELECT Statement 🧠

The `SELECT` statement is your primary tool for interacting with your database and retrieving the data you need. Here's its basic structure:

```sql
SELECT column1, column2, ... 
FROM table_name;
```

- **`SELECT`**: Initiates the SQL command to retrieve data.
- **`column1, column2, ...`**: Specifies the columns you want to retrieve. Use `*` to select all columns.
- **`FROM`**: Identifies the table containing the data.
- **`;`**: Ends the SQL statement.

### Retrieving All Records 📋

To get a complete overview of your data:

```sql
SELECT * FROM data_table;
```

This retrieves all records from your table, giving you a full picture of your app's activity.

### Retrieving Specific Details 🔍

To focus on specific information, such as transaction amounts and categories:

```sql
SELECT amount, category 
FROM data_table;
```

This narrows down the view to just the "amount" and "category" columns, helping you analyze specific aspects of your data.

### More Resources:
- [SELECT Statement](https://www.w3schools.com/sql/sql_select.asp)

---

## Day 2: Advanced Data Retrieval - Wildcards and Comparison Operators 🎯

[Watch Video](https://youtu.be/T11d2ScMtk8)

Welcome back, data detectives! 🕵️‍♂️ In this lesson, we'll enhance your SQL skills with powerful techniques for flexible and targeted data retrieval.

### Wildcards (%) for Flexible Searching 🔍

Wildcards are your secret weapon for finding records with variations in wording:

```sql
SELECT * FROM records 
WHERE description LIKE '%keyword%';
```

- `%`: Matches any characters before or after the "keyword."

### Comparison Operators for Targeted Filtering 🎯

Filter records based on specific criteria:

```sql
SELECT * FROM transactions 
WHERE amount > 100;
```

#### Example: Filtering by Date Range

```sql
SELECT * FROM events 
WHERE event_date BETWEEN '2023-01-01' AND '2023-12-31';
```

### Combining Techniques for Powerful Queries 💪

Combine wildcards and comparison operators:

```sql
SELECT * FROM products 
WHERE name LIKE '%pro%' AND price >= 50;
```

### More Resources:
- [Wildcards](https://www.w3schools.com/mysql/mysql_wildcards.asp)

---

## Day 3: Mastering the WHERE Clause - Filtering Data with Precision 🎯

Welcome back, data explorers! 🕵️‍♂️ In this lesson, we'll dive into the powerful `WHERE` clause, your tool for filtering data with precision.

### Understanding the WHERE Clause 🧠

The `WHERE` clause specifies conditions that records must meet to be included in the results:

```sql
SELECT column1, column2 
FROM table_name 
WHERE condition;
```

### Using Comparison Operators 🔍

```sql
SELECT * FROM transactions 
WHERE amount > 100;
```

#### Example: Filtering by Date Range

```sql
SELECT * FROM events 
WHERE event_date BETWEEN '2023-01-01' AND '2023-12-31';
```

### Logical Operators for Advanced Filtering 🎯

- **`AND`**: Combine conditions.
- **`OR`**: Retrieve records meeting one or more conditions.
- **`NOT`**: Exclude specific data points.

#### Example:

```sql
SELECT * FROM users 
WHERE age > 18 AND country = 'US';
```

### Combining Techniques for Granular Control 💪

```sql
SELECT * FROM products 
WHERE name LIKE '%pro%' AND price >= 50 
OR category = 'electronics';
```

### More Resources:
- [WHERE Clause](https://www.w3schools.com/mysql/mysql_where.asp)

---

## Day 4: Organizing Data with the ORDER BY Clause 📊

Welcome back, data organizers! 📂 In this lesson, we'll explore the `ORDER BY` clause, your tool for sorting data in a meaningful way.

### Understanding the ORDER BY Clause 🧠

The `ORDER BY` clause helps you sort data retrieved by a `SELECT` statement:

```sql
SELECT column1, column2 
FROM table_name 
WHERE condition 
ORDER BY column_name ASC|DESC;
```

- **`ASC`**: Sorts data in ascending order (e.g., A-Z, 0-9).
- **`DESC`**: Sorts data in descending order (e.g., Z-A, 9-0).

### Sorting by a Single Column 📋

```sql
SELECT * FROM records 
ORDER BY date DESC;
```

### Sorting by Multiple Columns 📑

```sql
SELECT * FROM records 
ORDER BY category ASC, date DESC;
```

### Key Note 🎯

The `ORDER BY` clause enhances clarity and usability by organizing data meaningfully.

### More Resources:
- [ORDER BY Clause](https://www.w3schools.com/mysql/mysql_orderby.asp)
