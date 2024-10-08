'''
Instructions

Please attempt the below tasks before you continue, so you can check and compare your answers with our solution.

Task 1: Create a database called bookshop. 

Task 2: Create a table called customers with customer ID, name, and address.  

Task 3: Insert a record of data for one customer. 

Task 1: Create database

Inside the terminal, write the “CREATE DATABASE” command followed by the name of your new database. In this case, the database name is called “bookshop”. Finally, add a semi-colon at the end of the statement and press Enter on the keyboard to execute the query. 

CREATE DATABASE bookshop;

Task 2: Create table

1. To create the customers table inside the bookshop database, you need to first choose the bookshop database by typing:

USE bookshop; 

2. Write the create table statement.

Write an SQL statement that contains the CREATE TABLE command followed by the name of the table, which is “customers” in this case. Then add an open parenthesis to define the table’s columns including the customer ID, customer name and customer address.

Of course, each column must be assigned a suitable datatype. Once all required columns have been defined, you must add a closing parenthesis and a semi-colon at the end of the SQL statement as follows:

CREATE TABLE customers (customerID int, customerName varchar(50), customerAddress varchar(255));

3. Click enter to execute the SQL statement. The output result below confirms the query is OK, which means the table has been successfully created.

4. To show the table you have already created, you can simply type:

SHOW tables;

The customers table is shown as part of the tables in the bookshop database.

Task 3: Insert data

1. Now, let's add our first customer data to the customer table! This can be done by writing the following SQL statement, which inserts a set of relevant values that each correspond to a specific column. Please verify that your create statement values reflects the defined data type of your columns and list values in the right order.

INSERT INTO customers (customerID, customerName, customerAddress) VALUES (1, "Jack", "115 Old street Belfast");

In this statement, you declare the INSERT INTO clause, followed by the name of the table. In this case, it’s “customers”  table. Then you add the column names within a pair of parentheses. Next, you insert the VALUES keyword and then add the values you want to assign to each column within a pair of parentheses. In this case the ID is 1, the name is "Jack" and the address is "115 Old Street, Belfast". Notice all VARCHAR columns values must be written within double quotations, whereas numbers do not require that.

3. You can type the following select SQL statement to get the content of the customers table after inserting the data.

SELECT * FROM customers;

Additional task (optional)

Mr. Ericson wants to insert another record of data for another customer, with the following details: the ID is 2, the name is "James" and the address is "24 Carlson Road, London". Your task now is to add the customer's details into the customer table.

Solution:

Write the following SQL statement in the SQL editor in your terminal, then press the Go button to execute it.

INSERT INTO customers(customerID, customerName, customerAddress) VALUES (2, "James", "24 Carlson Rd London") ;
'''