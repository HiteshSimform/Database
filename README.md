# Database
- Database Architecture

### Database Architecture
- T1 Architecture
- T2 Architecture
- T3 Architecture

Certainly! Here's the entire content, including SQL setup, data insertion, queries, and explanations, in one complete `README.md` format:

```markdown
# Employee Database Management System

This repository contains the SQL script to manage an employee database with basic operations, including table creation, data insertion, and queries for fetching employee information.

## Database Setup

### Create Database

```sql
-- Create Employee Database
CREATE DATABASE employee
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_IN'
    LC_CTYPE = 'en_IN'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
```

This command will create a new database called `employee` with specified configurations.

### Create Tables

The database includes two main tables:
1. `EmployeeInfo`: Contains general employee details such as name, department, project, etc.
2. `EmployeePosition`: Contains details about the employee's position, date of joining, and salary.

```sql
-- Create EmployeeInfo Table
CREATE TABLE EmployeeInfo (
    EmpID int PRIMARY KEY,
    EmpFname varchar(50) NOT NULL,
    EmpLname varchar(50) NOT NULL,
    Department varchar(50) NOT NULL,
    Project varchar(50) NOT NULL,
    Address varchar(50) NOT NULL,
    DOB DATE NOT NULL,
    Gender varchar(1) NOT NULL
);

-- Create EmployeePosition Table
CREATE TABLE EmployeePosition (
    EmpID int PRIMARY KEY REFERENCES EmployeeInfo(EmpID) ON DELETE CASCADE,
    EmpPosition varchar(50) NOT NULL,
    DateOfJoining DATE NOT NULL,
    Salary numeric(10,2)
);
```

### Insert Sample Data

Insert sample records into the tables `EmployeeInfo` and `EmployeePosition` to simulate real data.

```sql
-- Insert Data into EmployeeInfo Table
INSERT INTO EmployeeInfo VALUES
(1, 'Sanjay', 'Mehra', 'HR', 'P1', 'Hyderabad(HYD)', '1976-12-01', 'M'),
(2, 'Ananya', 'Mishra', 'Admin', 'P2', 'Delhi(DEL)', '1968-05-02', 'F'),
(3, 'Rohan', 'Diwan', 'Account', 'P3', 'Mumbai(BOM)', '1980-01-01', 'M'),
(4, 'Sonia', 'Kulkarni', 'HR', 'P1', 'Hyderabad(HYD)', '1992-05-02', 'F'),
(5, 'Ankit', 'Kapoor', 'Admin', 'P2', 'Delhi(DEL)', '1994-07-03', 'M');

-- Insert Data into EmployeePosition Table
INSERT INTO EmployeePosition VALUES
(1, 'Manager', '2022-05-01', 500000),
(2, 'Executive', '2022-05-02', 75000),
(3, 'Manager', '2022-05-01', 90000),
(4, 'Lead', '2022-05-02', 85000),
(5, 'Executive', '2022-05-01', 300000);
```

### Sample Data Preview

You can preview the inserted data using the following SQL queries:

```sql
-- Select all records from EmployeeInfo Table
SELECT * FROM EmployeeInfo;

-- Select all records from EmployeePosition Table
SELECT * FROM EmployeePosition;
```

---

## SQL Queries

Below are a series of SQL queries that perform various operations on the `employee` database.

### 1. Fetch the Number of Employees in 'Admin' Department

```sql
SELECT count(Department) 
FROM EmployeeInfo
WHERE Department = 'Admin';
```

### 2. Retrieve the First Four Characters of Employee's Last Name

```sql
SELECT EmpLname, LEFT(EmpLname, 4) 
FROM EmployeeInfo;
```

### 3. Find Employees Whose Salary is Between 50,000 and 100,000

```sql
SELECT eif.EmpFname, eif.EmpLname, epos.Salary
FROM EmployeePosition AS epos
JOIN EmployeeInfo AS eif ON eif.EmpID = epos.EmpID
WHERE epos.Salary BETWEEN 50000 AND 100000;
```

### 4. Find Employees Whose First Name Begins with 'S'

```sql
SELECT EmpFname 
FROM EmployeeInfo
WHERE EmpFname LIKE 'S%';
```

### 5. Fetch Top N Records Ordered by Salary (Top 3 Records Example)

```sql
SELECT * FROM EmployeePosition
ORDER BY Salary DESC
LIMIT 3;
```

### 6. Exclude Employees with First Names "Sanjay" and "Sonia"

```sql
SELECT * 
FROM EmployeeInfo
WHERE EmpFname NOT IN ('Sanjay', 'Sonia');
```

### 7. Department-wise Count of Employees Sorted by Employee Count

```sql
SELECT Department, COUNT(*) AS empCount 
FROM EmployeeInfo
GROUP BY Department
ORDER BY empCount ASC;
```

### 8. Create an Index for a Particular Field and Show Data Fetching Difference

#### Before Index Creation

```sql
SELECT empID, empFname 
FROM EmployeeInfo
WHERE Department = 'Admin';
```

![Description of Image](https://github.com/HiteshSimform/Database/blob/master/Assignment/output/before_index.png)

#### After Index Creation

```sql
-- Create Index on empID and empFname
CREATE INDEX idx 
ON EmployeeInfo (empID, empFname);


-- Query After Index Creation
SELECT empID, empFname 
FROM EmployeeInfo
WHERE Department = 'Admin';
```
![Description of Image](https://github.com/HiteshSimform/Database/blob/master/Assignment/output/create_index.png)

![Description of Image](https://github.com/HiteshSimform/Database/blob/master/Assignment/output/after_index.png)

## Indexing Performance

Creating an index on columns used in queries can significantly improve query performance. You can observe the difference in data fetching before and after creating an index on `empID` and `empFname` fields. An index speeds up the query execution by allowing the database engine to quickly locate the required data.

---

## License

This project is licensed under the MIT License.
```

This complete `README.md` file contains all the necessary setup, including database creation, data insertion, and queries. It is structured in a way that guides the user step by step through the process. You can use this for documentation or in any project related to the `employee` database.