'''
If you want to retrieve the data for the employee whose ID value is 1, you can use this SELECT statement. 

SELECT * FROM employee WHERE employee_id = 1; 

In this example, you need to retrieve the data for the employee whose name is James. You can use the equal operator in the WHERE clause condition.

Using the inequality operator

The inequality operator does the opposite of what the equal operator does. It compares two non-null expressions and returns true if the value of the left expression is not equal to the right one. If not, it returns the value of false.

There are two ways in SQL in which it can be used, <> or != and both methods result in the same outcome. 

For example, let’s say you want to determine which employee receives a salary that does not equate to 24000. You can use the following SQL statement:

SELECT *  

FROM employee 

WHERE salary <> 24000;

You can run the same query just by replacing <> with !=. It should behave in the same way and give the same result.

Using the greater than operator
This comparison operator compares two non-null expressions and returns true if the left operand is greater than the right operand. If not, the result is false. Let’s say you want to find out which employees are earning a salary of over 50000. You would write the SQL SELECT query as follows using the greater than comparison operator.

SELECT *  

FROM employee 

WHERE salary > 50000;

Using the greater than or equal operator
The greater than or equal operator (>=) compares two non-null expressions. The result is true if the left expression is a value that is greater than the value of the right expression. This time let’s say you want to see who pays a tax amount of 2000 or more. This is the query that will give the desired result using the greater than or equal operator:

SELECT *  

FROM employee 

WHERE tax >= 1000; 

Using the less than operator
The < operator in SQL can be used to test for an expression which is less than. That is, it compares two non-null expressions. The result is true if the left operand evaluates to a value that is lower than the value of the right operand. If not, the result is false. 

For example, let’s say you want to determine which employees get an allowance below 2500.

The following SQL query can be used to retrieve the result.


SELECT *  

FROM employee 

WHERE allowance < 2500; 

Using the less than or equal operator
In SQL, the <= operator tests for an expression less than or equal to. That is, it compares two non-null expressions and returns true if the left expression has a value less than or equal to the value of the right expression. If not, it returns true. 

You’d use it, for example, if you want to determine which employees have worked for less than or equal to 10 hours. The following syntax is an example of how you would use the less than or equal operator in the WHERE clause of the SELECT statement:

SELECT *  

FROM employee 

WHERE hours <= 10; 
'''