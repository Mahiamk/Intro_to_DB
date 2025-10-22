CREATE DATABASE IF NOT EXISTS employees;
USE employees;

CREATE TABLE Employees (
  employee_Id INT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  department VARCHAR(50) UNIQUE,
  hireDate DATE
)