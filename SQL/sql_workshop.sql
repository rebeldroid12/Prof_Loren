/*ex1*/
create  database  sql_workshop;

/*for mysql*/
use sql_workshop;

/*change into sql query for database sql_workshop*/

/*ex2*/
create table customers
(
customerid int
, customername varchar(100)
, address varchar(100)
, city varchar(50)
, zipcode varchar(5)
);

select * from customers;


select customername
, city
from customers;

/*ex3*/
insert into customers values (1, 'Charles', '200 LaSalle', 'Chicago', '60605');
insert into customers values (2, 'Charles', 'Wall Street', 'New York', '10001');
insert into customers values (3, 'Nancy', 'Blue St', 'Chicago', '60640');
insert into customers values (4, 'John', 'Blue St', 'New York', '10000');
insert into customers values (5, 'Wolf', 'Wall St', 'New York', '10001');

select * from customers;

/*ex4*/
select customername, city from customers where city = 'Chicago';

select distinct zipcode from customers;

/*ex5*/
/*first run update statements, if you get an error in mysql run the sql_safe_updates command*/
set sql_safe_updates = 0;
update customers set zipcode='60605' where city='Chicago';
update customers set zipcode='?????' where city='New York'; 


select * from customers;

/*ex6*/
delete from customers where city = 'Chicago';

select * from customers;



/*ex7*/
select * from customers 
order by customerid asc;

select * from customers 
order by customerid desc;

select * from customers
order by customername desc;

select * from customers
order by customername asc;


select * from customers
order by address, customername;
