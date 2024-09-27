'''
By now, you should be familiar with the concept of projects and apps in Django. You also explored the core files that make up a Django project. In this video, you will learn how to create your first Django project using the terminal and the VS Code editor.

You will also learn how to set up the development environment, by installing a virtual environment, and you will explore some common CLI commands used to create Django projects and launched the development server.

If you are a Python developer working on multiple projects, It's best practice to keep your projects isolated in a virtual environment, which you may be wondering why you need to do this. Well, Django projects can often be quite large and involve specific dependencies for things like packages. For example you could have a package that has a dependency on a specific version. 

You do not want this conflicting with your other Python or Django projects so it's best to keep your projects isolated using a virtual development environment.

Virtual environments are isolated spaces you create to manage dependencies and the overall project.

This allows you to keep features such as the interpreter, libraries and scripts isolated and installed for a specific project. In addition to the functionalities provided, Django also comes with an integrated development server.

This means that the application has a request response relationship with a client. Now that you are familiar with the concept of the virtual development environment and development server let's explore the steps involved in creating a Django project.

First, you create a project directory. Next, you create a virtual environment for your Django application. Then you create a Django project and finally run the Django development server. Let's explore each of these steps now in a little more detail using some examples in VS Code.

Your project is an organizational unit that consists of settings and database information. It can be stored anywhere on your development computer but as a best practice, it's best to keep it in a sub-folder with all your other Django applications.

First, open a new terminal by choosing terminal, new terminal from the top menu. Next, create a new directory by using the make directory command and then give your directory a name like build Django. Then enter inside this directory using the change directory command.

Next, you need to set up the virtual environment to do this, type Python 3-m and then venv. (python3 -m venv tutorial-env)

Then give the virtual environment a name such as tutorial-env. Once you are finished, press "Enter." 

If you open the directory structure in VS Code, notice that some new files have been generated. Now you need to activate the virtual environment type source and the path from where you can activate it, which is tutorial-env, then activate and press "Enter."  source tutorial-env/bin/activate

Notice that the virtual environment is activated by the round brackets suffix in the terminal.

Once the virtual environment package is installed, you are ready to install Django, and you do this by using the command pip3 install Django. (pip3 install django)

To make sure that Django is installed, you can run the command Python3 -m Django version. Notice that the current version is 4.1. Once this is set up, you are ready to create a project, and you do this by running Django's built-in command line tools.

Type Django admin, start project, and then give the project a name (django-admin  startproject chefstable). In this example, it's shifts table finally, press "Enter" to run the command. If you expand the directory structure again, notice that the shifts table is created with supportive Django specific files.

Once your Django project is created, you need to launch the development server. Before you do this, it's important to be aware of the manage.py file that is automatically created with the project. Recall that manage.py is a command line utility that works like the Django admin command.

You can replace the Django admin command with manage.py as it uses the project settings. To launch the development server you can run the run server command using the manage.py command. You will learn more about how to work with Django admin, and manage.py commands later. (inside the project folder: python3 manage.py runserver)

In this video, you learned how to create your first project in Django using the terminal VS Code, and Django is built-in command line tools.
'''