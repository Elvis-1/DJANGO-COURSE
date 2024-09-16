'''
By now, you should be familiar with the core structure of the Django framework. You know that to create a Django application, you need to create a virtual environment for the project. 

Create the project, and then run the development server. You do this by running specific commands such as start project and run server using the Django admin command line utility.

Django provides a set of commands that also generates a project structure, that contains the configuration and settings related to the entire web application. 


When working on Django projects, developers have two choices for command line utility to perform tasks. They can use either Django admin or manage.py. While both can be used to perform the same tasks, there are some subtle differences, and your choice of usage will depend on how you want to work on your project.

In this video, you will learn about the Django admin and manage.py commands, and how developers use them to perform administrative tasks.

One of the powerful features of Django is that it provides a ready-to-use admin interface, in the form of a command line utility named as Django admin.

Django admin is Django's command line utility for administrative tasks. This utility is present in the scripts folder of the Django environment directory. 

The Django admin utility is executed from inside the terminal. Manage.py is a script that is the local version of Django admin and is located inside the project folder.

 It sets the Django settings module environment variable so that it points to your project settings.py file. 

Django admin is a file that is created when you install Django. The Django admin utility should be on your system path, if you installed Django via pip, if you do not find it on your system path make sure you have your virtual environment activated, and install Django inside it using a command such as pip3 install Django.

Manage.py is a file that is automatically created each time you create a Django project, this file is specific to the virtual environment of the project. It does the same thing as Django admin but also sets the Django settings module environment variable to point to your project's settings.py file

Generally, when working on a single Django project, developers tend to use manage.py as the administrative tasks of Django admin can also be performed with manage.py.

However, if you need to switch between multiple Django settings files, use the Django admin command with the Django settings module or the settings command line option.

The command line examples throughout this video use Django admin to be consistent. But any example can use manage.py just as well.

You may recall that you use the start project command to create a Django project.

This creates a Django project directory structure for the given project name in the current directory or the given destination. 

By default, the new directory contains the manage.py file and a project package. This project package contains a settings.py file and other files. It's important to know that if only the project name is given, both the project directory and the project package will use the same name as the project name.

Also, the project directory will be created in the current working directory. If an optional destination is provided, Django will use that existing directory as the project directory and create the manage.py file and the project package within it.

A common developer workflow is to use the period symbol to denote the current working directory, this avoids having sub-directories with the same name. Recall that you use the run server command to run a project.

This command starts a lightweight development web server on your local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. However, it is possible to change this as you can pass in an IP address and port number explicitly. 

It is important to know that if you run this script as a user with normal privileges, which are recommended, you might not have access to start to port on a low port number. This is because low port numbers are reserved for the superuser or root user. 

The development server works great for application development and testing. However, Django recommends that you should never use this server in production, as it has not gone through security audits or performance tests. 

The development server automatically reloads Python code for each request as needed. You don't need to restart the server for code changes to take effect.

However, some actions like adding files don't trigger a restart, so you'll have to restart the server in these cases. 

In this video, you learned about the Django admin and manage.py commands, and how developers use them to perform administrative tasks.
'''