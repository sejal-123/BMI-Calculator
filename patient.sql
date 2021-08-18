use internship;

create table if not exists patient(
pid int primary key auto increment,
name varchar(50),
age int,
phone varchar(10),
gender enum('m', 'f'),
bmi double
date DATE
);