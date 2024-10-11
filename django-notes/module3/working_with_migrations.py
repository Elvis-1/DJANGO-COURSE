'''
In this video, you will learn
how to apply migrations in a Django project using the commands makemigrations
and migrate. You will also learn
how migrations allow developers to apply
version control to the models and explore the generated sql using
the command sqlmigrate. I've already created
a project in VS code containing
an app called myapp. Inside the models.py file, I've created a class
called Menuitems. Recall that this class
is equivalent to a table in sql and contains
three attributes, name, course, and year
with respective fields.

Before I began
applying migrations, I have to ensure that I have
updated the model inside the settings.py file inside
the project folder. When I open that file, notice that I've
added the app inside the INSTALLED_APPS list,
so I'm good to go. Back in the models.py file, the first thing I need to
do is make the migration. So I run the command python manages.py and then
make migrations. I press "Enter" and Django displays a message
saying that it will make migrations for my app and create a model called
Menuitems inside it. Also, it will create a file with the name 0001_ initial.py. Next I need to apply
the migration.

I run the command python manages.py migrate
and press "Enter". This time, notice that Django performs migrations
with this command. Just so you're sure, let me explain the difference
between these two commands. MakeMigrations is
Django's way of preparing the changes to
be made in the model. For example, it creates
a database such as this one named db.sqlite3. So you can think
of makemigrations as the command that generates the sql commands and migrate as the command where those
sql commands are executed. In this video, I will not be adding any data to these tables.

I only want to modify
the columns inside a table by modifying the
attributes in the model. Once I've run this command, notice that a folder called migrations is created
inside the app folder, which consists of the file that keeps a record of
the migrations.

If I open the file, notice that the code contains
the table columns, names, and auto assigned
primary key called ID. So now you know the
commands makemigrations and migrate are used to perform
migrations in Django. However, what if I want to make some changes to the model? For example, suppose
I want to change the attribute course to
category and save this file. For this change to take effect, I have to run the
makemigrations command again. Notice that Django displays
a message that asks, "Was menuitem.course renamed
to menuitem.category?" To confirm, I type yes
and press "Enter". Now, notice that another file is created inside the
migrations folder. If I open that file, notice that it contains the code changes performed
in that migration.

I want to make another
change to the model so I open the
models.py file again. This time I will change the
attribute name to item name. So I will save the file
and rerun the migration. I confirm the change by typing y and notice that
Django displays a good description
of the changes I've made in addition to the
new file that's created. Now you know how to
change the model using the
makemigrations command. Suppose I want to display all the migrations
that I performed. 

To do this, I can run
the command python manages.py and then
show migrations. Let me expand the terminal. Notice that under the
name of the app, myapp, the three migrations I
performed are displayed. The X symbol represents the
commits to the migrations. Since I have not executed the migrate command
for my latest changes, notice that the last
place holder is empty. Let me run the migrate
command again. When I show migrations, the X appears in front
of all three files. Now suppose that after
making the changes, I want to revert back to a
migration I performed earlier. I can do this by typing
python manage.py migrate, then I need to specify the name of the app
and the final number, for example, 0001. But before I execute, I can add a flag such as plan. 


Django will then display the
changes it will revert to. In this example, it'll
change the attributes of menuitems_itemname back to name, and category back to course. This time, I execute this
command without the plan flag. And notice that
even if the changes are not displayed
in the Python file, the changes have been reflected in the database I created. The final command I want you to know about is sql migrate. 

I can run this command against
some migrated version. Notice that when I execute it, the corresponding
sql commands are displayed for the migrations
I have performed. In this example, I ran it
against the third migration. Notice the sql alter
statement on the table named menuitems to rename the
column from name to itemname.

I can run this command against
some migrated version. Notice that when I execute it, the corresponding
sql commands are displayed for the migrations
I have performed. In this example, I ran it
against the third migration. Notice the sql alter
statement on the table named menuitems to rename the
column from name to itemname.

'''