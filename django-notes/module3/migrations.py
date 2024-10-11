'''
In the world of web application development, application requirements constantly change and it's a developer's job to implement these changes. For example, a common task is to alter the data model of the application. To do this in Django, you use something called migrations. In this video, you will learn about migrations in Django and how developers use them to make changes to the models representing the database schema. 

Recall that Django is designed to work with a relational database management system like PostgreSQL, MySQL, or SQLite, and in a relational database, data is organized in tables. By now, you know that you can use models to represent data tables stored in the database.

Recall that when using models, Django provides many methods that allow you to add, update, and delete data right from the code without having to write SQL. This is made possible by using something called an object-relational mapper, or ORM. You will learn more about this later.

For now, just know that it maps the relational database to objects represented as Django models. The models define the database fields which correspond to the columns in their associated database tables. For example, if you have a model called User, you know it will represent a table called User and each attribute of the model has a column representation in the database.

In the Python code, if the user class has an attribute of first_name, the table will have a column of first_name. It's common that during the life cycle of the development of the application, changes to the structure of the database or schema will be required. For example, the initial model may need to be extended with additional attributes. 

This means adding a new attribute, which will add a new column from the perspective of the database. Or, suppose you need to perform a different operation, like changing a column name or even deleting a model. For these operations to work, Python uses something called database migrations. 

Migrations are how Django records changes made to models and implements these changes to the database schema. Migrations are tied into Django models and stored as migration files in a Migrations folder inside each app. You will learn more about migration storage later. 

For now, let's explore how migrations work and return to the example of the Users table. Suppose you wanted to add a new column called City to the User table. Without an ORM like the one Django provides, a developer must login to the database and run a SQL alter statement. You may recall that you can use the alter statements to alter a specific table to add a column of whatever type is required. When the statement runs, the User table updates with another column called City.

In Django, the User table is created using a model which you may recall is a class-based representation of the User table in the database. So instead of writing the SQL query, you only need to add the new attribute to the model then run the migration scripts to implement the changes. Once the migration scripts run, the changes are applied. Let's explore the process of running the migration script a little further now.

Django provides a list of CLI commands that allows you to apply the migrations. First, you must create a migration script and then apply the migrations. The migration script is a set of instructions on what models to create against the database. You apply the change to the model, run the migration file, and Django will take care of the rest. You do not need to write any SQL as the application handles everything.

Later in this lesson, you will learn more about running a migration script and applying it to the database. For now, let's focus on some of the reasons developers use migrations instead of SQL. You may wonder why you need migrations when it appears straightforward to just run a SQL query like the earlier example to update a table. 

Migrations do more than just implement SQL commands. They can help with syncing issues, version control, and database maintenance. It's good to think of migrations as a version control system for your database schema. Let's explore some of those benefits in more detail now, beginning with syncing issues.

With migrations, you have less possibility of syncing issues between what the model has and what the database contains. When working in a team, each developer usually has their own local copy of the database so they can code and test against it. Migration scripts are kept in the code repository. When a developer on the team makes changes, they run the migration script to update their local copy of database to the latest version.

Next is version control. All the changes are kept in version control, which provides an entire history of changes across the application. Developers can also use this to determine what changes have been added and by whom. Generally in application development, the more you can track changes that occur in the app, the fewer problems you will encounter.

The alternative is running scripts in the database directly, which is usually more problematic as it is outside version control. The last benefit of using migrations is the ease of maintenance. Along with helping syncing issues and version control, maintaining all the database changes from the code base makes it easier for the development team. They don't have to worry about creating SQL queries directly against the database or where to store these files so all the developers can run them. In this video, you learned about migrations in Django and how developers use them to make changes to the models representing the database schema.


'''