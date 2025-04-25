# Data Manipulation Language (DML) 💾

In SQL, Data Manipulation Language (DML) is used to manage and manipulate data stored in the database. DML statements allow you to perform various operations like inserting new data, updating existing data, or deleting unwanted data. It provides a way to interact with the actual data in the database.

## The INSERT Statement

The `INSERT` statement allows you to insert one or more rows into a table. The following illustrates the syntax of the `INSERT` statement:

```sql
INSERT INTO table_name(column1, column2,...) 
VALUES (value1, value2,...);
```

### Explanation:
1. **Table Name and Columns**: Specify the table name and a list of comma-separated columns inside parentheses after the `INSERT INTO` clause.
2. **Values**: Provide a comma-separated list of values corresponding to the columns inside the parentheses following the `VALUES` keyword.

**Note**: Ensure that the number of columns matches the number of values, and their positions correspond precisely.

---

## The UPDATE Statement

The `UPDATE` statement updates data in a table. It allows you to change the values in one or more columns of a single row or multiple rows.

### Syntax:
```sql
UPDATE table_name 
SET 
    column_name1 = expr1,
    column_name2 = expr2
[WHERE condition];
```

### Explanation:
1. **Table Name**: Specify the name of the table to update after the `UPDATE` keyword.
2. **SET Clause**: Specify the columns to update and their new values. Use a list of comma-separated assignments for multiple columns.
3. **WHERE Clause**: Optionally, specify which rows to update using a condition. If omitted, all rows in the table will be updated.

**Caution**: Always use the `WHERE` clause carefully to avoid unintentional updates to all rows.

---

## The DELETE Statement

The `DELETE` command is used to delete data from a table.

### Syntax:
```sql
DELETE FROM table_name WHERE condition;
```

---

## More Resources:
- [INSERT](https://www.w3schools.com/SQl/sql_insert.asp)

---

# DAY 2: 💧 ACID Properties of Transactions 💧

Transactions follow four key properties to ensure accuracy and reliability, called **ACID**. Each part of ACID plays a role in making sure that database transactions happen smoothly and safely. Let’s explore these properties with an example: a mobile money transfer! 📲💰

### 🌟 A - Atomicity: “All or Nothing”

Atomicity ensures that all parts of a transaction are completed together as a single unit. If one part fails, none of the transaction’s changes are saved.

**Example**: Transferring Ksh 1000 from Alex’s account to Bella’s account:
1. Deduct Ksh 1000 from Alex’s account.
2. Add Ksh 1000 to Bella’s account.

If either step fails, the transaction is rolled back, ensuring no partial changes occur.

---

### 🌐 C - Consistency: Keep It Accurate

Consistency ensures that transactions do not violate database rules or constraints, maintaining data accuracy.

**Example**: If Alex has only Ksh 500 and tries to send Ksh 1000, the transaction is rejected to maintain the rule that no account can have a negative balance.

---

### 🔒 I - Isolation: No Interference

Isolation ensures that transactions are processed independently, without interference.

**Example**: If Alex is sending money to Bella while Charles is transferring money to David, isolation ensures these transactions don’t affect each other.

---

### 🔐 D - Durability: It’s Permanent!

Durability ensures that once a transaction is committed, its changes are saved permanently, even in case of system failure.

**Example**: After Alex transfers Ksh 1000 to Bella:
- Alex’s balance decreases to Ksh 0.
- Bella’s balance increases to Ksh 2000.

Even if the system crashes, these changes remain intact.

---

## More Resources:
- [ACID](https://www.geeksforgeeks.org/acid-properties-in-dbms/)