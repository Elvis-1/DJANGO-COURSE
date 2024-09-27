'''
Most websites or web applications provide a homepage when you type in the name of the URL or click on the website link from a search engine. The homepage is returned when only a request for a URL with the domain name is sent.

Previously, you learned that in order to accept a HTTP request and return a HTTP response, you need to create a view function inside the views.py file. The view function is then mapped to a URL and when the request to that URL is made, the view function will be called

In this video, you will learn about URL configuration in Django and how it's used to map URLs to views. You will explore the URL configuration file, urls.py, and learn why it exists at both the project and app levels. Finally, you will learn how to reference the urls.py file at the app level using the include function.

To design URLs for an app, you create a Python module informally called a URLconf or URL configuration. The URL configurations used by the view functions in Django are created and updated in the urls.py file. Django by default creates a urls.py file at the project level. But additionally, it's best practice to create a urls.py at the app level.

This way, the respective URLs for an app are clustered. But the project also needs to know what URLs are used inside each app. For example, in Django, when a user makes a request for a URL, this request is first handled by the urls.py file at the project level.

Django looks for the variable URL patterns. However, the code that contains the logic for the URL mapping is at the app level. You need a way to tell Django to also check the urls.py file at the app level. You do this by using the include function. In the urls.py file at the project level, you create a new path inside the URL patterns list.

Then inside the path function, you pass a reference to the app level urls.py file as the view argument. This allows the project level to access the app level URLs. By using the include function, the project level urls.py can inherit the app level URL configurations. You will explore this concept of inheritance in more detail later when you work with routes containing URLs represented as strings. 


Now let's open VS Code and create the code for the URL configuration. To begin, let's create a project and inside the project, create an app called myapp. 

To ensure that the Django app is running, launch the development server by running the terminal command python3 manage.py runserver. Now, select the URL to deploy Django to your local host. Notice that the webpage with a successful install message is displayed.

Let's close the webpage and stop the server for now. The first step is to open the views.py file to create a view. Using the import statement, type django.http import HTTP response. Next, create a function called home and pass the request object inside of it. Next, return an HTTP response containing a string. Let's use the example of the homepage for the Little Lemon restaurant.


The first step is to create a file inside myapp called urls.py. Recall that this is the app level urls.py file, and that one also exists at the project level. In the urls.py file, you need to import the path function from the Django dot URLs.

This allows you to use the path function inside the URL patterns list. It's inside the path function where you map the URLs to its relevant view function. The next step is to create the sequence called URL patterns. 

Between the open and close square brackets, you add the path function and inside the parenthesis pass an empty string followed by the location and the name of the view function. Because the file's urls.py file and views.py file are in the same folder, you only need to provide the name of the file without the.py extension where the view function is located, and then a dot and the name of the view function. 

Notice that VS Code highlights the word views in the code. This means that in order to use the views.py file, it must be imported. Type from.import views and save the file. It's important to remember to add a comma at the end of this path function to match the parsing that Django performs. 

Now, save the file once more. The code is nearly complete. The final step is to set the URL configuration at the project level. This is because the project file doesn't know where the view function is. To set this configuration open the urls.py of the project. 

Beside the keyword path type comma, and then include to import the include function. Next, inside the URL patterns list, add another path function. Inside of the parenthesis, pass an empty string. For the second parameter, use the include function to pass the location of urls.py file of the app. Once again, remember to not add the.py extension.

Save the file, and open the local host URL in the browser. Success. The message, Welcome to the Little Lemon restaurant displays. In this video, you learned about URL configuration in Django and how it's used to map URLs at the project level to views at the app level.
'''
