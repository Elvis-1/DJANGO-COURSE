'''
When you develop a web application, much of the content is stored somewhere like in a database. As a result, a common task is to provide an administration or admin site as part of the application.

The purpose of this admin side is to allow certain users to administer and manage the data of the application. In this video, you will learn how to activate Django's admin interface and how to use its core feature

You may remember this when you covered the topic where the path configurations for the admin were set by default inside the URL configuration files. Now, suppose the owners of Little Lemon have asked you to store all of the website content in a database so it can be updated by the restaurant staff. For example, managers can use the admin site to add or edit content. 

That content is displayed on the public site. For developers, building such as site for each project can be tedious work. Django solves the problem by automatically creating a unified admin interface for site administrators to add, edit and delete content, such as users, permissions and database entries. 

This process is automated as the admin interface directly links to the models in the project once registered. The admin interface is usually a part of a large web application to help the administrator perform certain administrative tasks. The tasks such as creating and managing users, controlling access permission, and forming user groups.

Django reads the models declared in the project and from the metadata of models declared in a project, it quickly builds an easy-to-use interface. It's important to remember that the admin site isn't intended to be used by site visitors. It's for site managers. In addition to the interface, another powerful feature of Django is that it provides a ready-to-use admin interface named Django admin.

As you have already learned, you use this command line utility for administrative tasks. The Django admin utility is executed from inside the terminal. It is enabled and assigned to a project by default when you run a command such as start project inside Django. 

As the admin interface depends on django.com.admin app, you'll find it in the installed app section of the settings.py file, along with certain other apps. Databases are an inherent part of building a web application. Using Django and Django admin provides a convenient means of accessing and modifying these databases from a friendly user interface.

Before you access this interface, you first need to create an admin user that provides you with the necessary credentials. Let's explore how to do that now and to have an overview of the Django admin interface. First, you must create a user. For that, run the command python3, manage.py, then add the keyword createsuperuser. Next, in the username prompt, you must create a username.

For example, add John and press "Enter". Notice that if a user is already created, Django will throw an error stating that the username is already taken. Now I create a user called Adrian and press "Enter". Next, another prompt appears for the email address. Let's type adrian@littlelemon.com and press "Enter". Then enter a password and press "Enter".

Notice that because this is not a strong password, Django displays a warning stating that the password should be more secure. You can ignore this for now and press Y, which stands for yes. This will let us continue. But it's important to know that in a real-world application, the password should be strong and meet security requirements. Once you create the superuser, run the command to run the server and open the default URL in the browser. 

Next, go to the assigned path and add forward/admin to the URL and press "Enter". Notice that the Django administration page loads with the login form where you are prompted to enter username and password. Type the username and password that you created earlier and click the Login button. After logging in, notice that there is a basic interface.

The first option gives an overview of the groups and users. There is already a sample model named reservations. Below that, there is a list of recent actions which are empty at the moment. You have an option to add and change these configurations. If, let's say you go to the reservations model and click "Change", notice that there are a few entries listed. You have an option to directly update the reservations data using the form or add new entries. You can also delete the selected reservation by clicking the checkbox next to the names. If you go back to the main page, there are other options to add or modify the users that already exist. For example, if you click a specific user, you can change the username and password, the personal info, and also assign the user to some groups.

Additionally, you can designate specific permissions that the user can have, which would be listed below. There are also other additional details such as last login information and days of joining for the user. You can also go to the top of the page and check the history of the user and the changes they have made.

The utility of this might not be immediately evident. But as you proceed in the course, you will realize how using the Django admin panel can save a lot of time for the developer by providing an interface that is easy to modify inside your project and model. In this video, you learned how to start Django's admin interface site. 

You also learned how it can be used to add users, groups, models, and assign permissions, which you will learn more about later. Good job.
'''