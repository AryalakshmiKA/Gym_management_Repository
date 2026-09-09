create database companydb;
use companydb;
create table employee(
id int primary key auto_increment,
name varchar(100),
place varchar(100),
mobile varchar(15) unique,
email varchar(100),
department varchar(100),
salary int,
joining_date date
);