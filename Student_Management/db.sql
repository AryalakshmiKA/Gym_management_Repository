create database student_db;
use student_db;
create table student(
id int primary key auto_increment,
name varchar(100),
place varchar(100),
mobile varchar(15) unique,
email varchar(100),
department varchar(100)
);