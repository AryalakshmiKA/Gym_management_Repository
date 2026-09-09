create database gym_db;
use gym_db;
create table member(
	id int auto_increment primary key,
    name varchar(100) not null,
    place varchar(100),
    plan enum("1-month","2-months","6-months","12-months"),
	mobile varchar(15) unique,
    fee int,
    joined_on date
);