'''
Write the create table statement
To create the vehicle table, write an SQL statement that contains the CREATE TABLE command followed by the name of the table (vehicle in this case) and open parenthesis to define the table’s columns including the vehicle ID, owner ID, plate number and phone number. Of course, each column should be assigned a suitable datatype, as shown in the previous ER diagram.


CREATE TABLE vehicle(vehicleId varchar(10), ownnerId varchar(10), plateNumber varchar(10), phoneNumber varchar(10), PRIMARY Key (vehicleId));

To show the table you have already created, you can type the following syntax:

Show tables;

To show the structure of the vehicle table, you can type:

Show columns from vehicle;

Now any candidate key that has not been chosen to act as the primary key of the vehicle table is called an alternate key. That’s the plate number and phone number.


Also, it’s important to remember that a primary key can be composed of one single simple attribute or multiple attributes (a composite key), which is composed of two or more attributes that form a unique value in each row of the table. 


Now let’s build another table to maintain data about the vehicles’ owners. This table includes information about the owner's name and address as illustrated below.


CREATE TABLE owners(ownerId varchar(10), ownerName varchar(10), ownerAddress varchar(255), PRIMARY KEY(ownerId));

To create this relationship in the actual database you need to modify the vehicle table structure to make the owner ID a foreign key. This can be done by using the “ALTER” command to change the structure of the vehicle table. You can also use the "ADD” command to define the owner ID as the foreign key. Finally, you can use a "REFERENCES” keyword to reference it with the primary key in the owner table.



ALTER TABLE vehicle ADD FOREIGN KEY (ownnerId) REFERENCES owners (ownerId);



'''