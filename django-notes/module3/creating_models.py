'''
By now, you should be familiar with the concepts of models and how they're used to represent a table in the database. In this video, you'll learn how to create a model in the Models.py file. Okay, so I'm in VS Code and I've already created a project called menu project and an app called menuapp.


To build a model, I write code in the Models.py file, so let me open that now. Notice that there's already a comment that says create the models, so I will add the code under it. For this example, suppose I'm building a menu for the little lemon restaurant. 

First I create a class name Menu and pass the model into it.

Inside the class, I will create three variables. The first variable is the name of the item, the second variable is cuisine and the third variable is price. These are the attributes inside the model and each of these attributes needs a field of some data type. So I assigned a field by typing models.CharField which is used for small to large size strings. I can also pass a perimeter such as max length and assign a value like 100. I will repeat the same process for the cuisine variable. For the price, I type models.IntegerField which I can use to store an integer value.

Notice that I don't have to pass anything to it. Okay, that's all the code I need to write for the model, now let me try accessing it. In the terminal, I type the command python manage.py shell and press Enter.

Notice that I enter the command line tools of django. It's important to know that I cannot directly access the class menu inside the shell. First, I have to import it from another python file called models.py inside the menuapp folder. I do this with the import python command where menuapp is the folder and models.py is the file.

So from inside that I import the menu, I press Enter and notice that I get an error.

This is because I have not added the model inside the settings.py file. So, let me open that file now and add the model to the installed apps list. Okay, so once I've added the model to the installed apps list, I need to perform something called migrations. Don't worry too much about this step, you'll learn all about migrations later. For now, just know that this is a command I need to run to work with models in django. 

Notice that it creates a model, menu and a python file. If you go to the python file, you can see that django internally has created the columns and the table menu using the built in SQLite database. To finish this step, I run another migration command by typing python manage.py migrate. Okay, so now I'm ready to go back inside the shell and work with the menu model I created, let me first clear the terminal.

I run the command python manage.py shell and once inside I import the menu again, this time notice I don't get an error. I can now run the command menu.objects.all which returns all the entries in the database. Since I don't have any notice that I get an empty query set. I will now directly add an entry in the database using the command m equals Menu.objects.create.

I enter the details that match the attributes, so name equals pasta, cuisine equals Italian and price equals 10. Notice that I've assigned this entry to an object m. And that is so I can manipulate changes on the objects such as updating or saving, I press Enter and now I save this object. Now if I run the command to return all the entries in the database again, notice that one entry is inside the database. Okay, let me add one more entry quickly and view the database entries again.

Notice that there are two objects but this is not very informative as only the names of the menu objects one and two are displayed. Django provides a way to change this using something called custom methods. For example, I can use one of the building custom methods and customize the string. So let's say that I type self.name plus str which represents a Dunder method that prints a string.

I will save the file, once I do this I must exit the shell and enter it again. Once inside the shell, I can write python code exactly like I would write in a file. I import the menu class again and run the command to display the items again. Notice that the details are printed in line with the string Dunder method with a custom function I defined. Similar to this, I can create my own custom functions that can be used. Now that I've demonstrated how to create a database table and add entries to it, let me demonstrate how to update entries. 

Suppose I want to access an entry and update it. To do this, I can use the get method and pass the primary key of value to which refers to the entry of taco.

Then I can assign this to an object that I created called p. I can now access the attributes inside this object just as I would in regular python code. Now I type p.cuisine equals and a new value to update the entry. I save this and this time when I display the entries, noticed that the value is updated. Another option to view and update the database is using your browser to access the django admin portal. However, it's also important to understand how the code works internally as I've demonstrated.


This video was just to give you an example of how you can use models. You'll learn more about migrations, the admin profile and other features you can add using django and python code within the models. In this video, you learned how to create a model in the models.py file.
'''