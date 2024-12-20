'''
Object Relationship Mapping - ORM

What is ORM 

Usually, the type of system used in an Object-Oriented language such as Python contains types that are non-scalar and every time, they cannot be represented only in primitive types such as integers and strings. 

On the other hand, data types in tables of a relational database are of primary types, that is integer and string. 

Therefore, the program needs to convert objects in scalar data to interact with a backend database.

Object-oriented programming languages use Object Relation Mapping (ORM) to interact with Structured Query Language (SQL), both of which are incompatible.

The ORM layer maps a class to a table in a relational database, with its attributes matching the table's field structure. 

The ORM library lets you perform the database operations in an object-oriented way instead of executing raw SQL queries. 

This allows you to focus more on the programming logic than the backend database operations.

Object Relational Mapping or ORM is the ability to create a SQL query using object-oriented programming language such as Python. This enables a quick turnaround time in fast production environments that need constant updates. 

Each model is a Python class that subclasses django.db.models.Model

Each attribute of the model represents a database field. Essentially you can think of a model as a Python object, and models help developers create, read, update and delete objects, commonly called the CRUD operations.

Django has its own ORM layer. Its migration mechanism propagates the models in database tables. 

You need to construct a QuerySet via a Manager of your model class to retrieve objects from your database.


QuerySet
Let's try to understand how QuerySet is constructed and handled with an example. To begin with, add the following models in the Django app named demoapp.

from django.db import models  
class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 

The idea is to create two tables, Customer and Vehicle, with a one-to-many relationship. Apply the migrations and you will see these two tables in the project's database.

Next, open the Interactive shell.

It is important to know that these commands are the same if you are on Windows or Mac.

(djenv) C:\djenv\demoproject>python manage.py shell 
Create an object of the Customer class. Give a string parameter to the constructor. The save() method of the models.Model class creates a row in the Customer table. 

>>> from demoapp.models import Customer 
>>> c=Customer(name="Henry") 
>>> c.save() 

Adding a model object
The Customer.objects gives the Manager of the model. It handles all the CRUD operations on the database table. For example, an object can also be created with the create() method as follows:

>>> Customer.objects.create(name="Hameed") 
<Customer: Customer object (2)> 

The create() method actually performs the INSERT operation of SQL.

Now, let us add two objects to the Vehicle model. Note that one of the fields in the Vehicle model refers to an object of the Customer table as ForeignKey. Fetch the Customer object with a primary key = 2.

>>> from demoapp.models import Customer, Vehicle  
>>> c=Customer.objects.get(pk=2) 
>>> c.name 
'Hameed' 

>>> v=Vehicle(name="Honda", customer=c) 
>>> v.save() 
>>> v=Vehicle(name="Toyota", customer=c)   
>>> v.save() 

>>> c=Customer.objects.get(name="Henry") 
>>> Vehicle.objects.create(name="Ford", customer=c) 
<Vehicle: Vehicle object (3)> 
>>> Vehicle.objects.create(name="Nissan", customer=c) 
<Vehicle: Vehicle object (4)> 

Fetch model objects

A QuerySet represents a collection of objects from your database. It represents a SELECT query. To fetch all the objects, use the all() method of the Manager.

model.objects.all()


The all() method returns a list of objects. You can iterate over it with the usual for loop or list comprehension technique.

>> lst=Customer.objects.all()  
>>> [c.name for c in lst] 
['Henry', 'Hameed'] 

You can apply filters to the data fetched from the model. This is used to fetch objects satisfying the given criteria. In SQL terms, a QuerySet equates to a SELECT statement, it is like applying a WHERE clause.

model.objects.filter(criteria) 

For example, use the following statement to retrieve all the customers with names starting with 'H'.

mydata = Customer.objects.filter(name__startswith='H') 

Similarly, you can retrieve the objects of the Vehicle model. Remember that the Vehicle object refers to a customer object. You can retrieve the attributes of the related customer as follows:

>>> lst=Vehicle.objects.all() 
>>> for v in lst: 
...     print (v.name, " : ", v.customer.name) 
...  
Honda :  Hameed 
Toyota :  Hameed 
Ford :  Henry 
Nissan :  Henry 

Updating and removing a model object
To update an object, such as changing the Customer's name from Henry to Helen, assign a new value to the name attribute and save.

>>> c=Customer.objects.get(name="Henry") 
>>> c.name="Helen" 
>>> c.save() 

Similarly, the delete() method of the model manager physically removes the corresponding row in the model's mapped table.

>>> c=Customer.objects.get(pk=4) 
>>> c.delete() 
(1, {'demoapp.Customer': 1}) 

This way, you can perform the CRUD operations on a database table using the QuerySet API instead of executing raw SQL queries.
'''