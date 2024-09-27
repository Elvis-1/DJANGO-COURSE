'''
By now, you should know that the request response cycle works between the client and server, in this video, you will learn how to use Djando's HTTP request and response objects. Let's now explore how the request response cycle happens inside Django.

The cycle begins when the user enters a URL in their web browser.

This URL is sent to the web server where Django searches for a match inside the urls.py file. Once it finds the URL, it is mapped to its associated view. Inside the view file, the view function receives the HTTP request as a request object. The view function then defines the appropriate HttpResponse and sends it back as a HttpResponse object. This response is processed by Django and the client receives the HttpResponse.

Let's now open VS Code and explore how to work with Django's request and response objects.

Open the views.py file and add the necessary imports. Next, create the view. Recall that Django uses the request and response objects to pass through the system.

The APIs for the HttpRequest and the HttpResponse objects, are specified in the django.http module and you use the request and response objects from this module inside the logic of the view function.

Now you're ready to create the view function. Create a view function named home and pass the request object to it. Select the urls.py file to ensure that the function name matches the view function inside the urlpatterns list. Return to the views.py file and access the path property inside the request object by typing request.path. Now, assign this to a variable named path

It's important to note that the format needs to be changed to return the path variable in the HttpResponse. The next step is to create the return statement with the HttpResponse object. Inside the parenthesis, pass that path argument, followed by the content type and finally the character set.

Save the file and open the local holes to URL in the browser, enter the exact location of the URL which is /main/home/.

Notice that the path is displayed in the main window of the browser and is the same as the order in which you pressed main and then home inside the urlpatterns list.

If you remove main in the urlpatterns list and save the file, you can configure the URL by removing the path main. Notice that the path updates to home, this is because Django so fixed the path provided from the app level to the current path inside the project level.

This example demonstrates that the HttpResponse behaves like an ordinary object

Let's explore this further by creating another HttpResponse object and assigning it to a variable called response. Pass the string with the message, this works. So instead of returning the HttpResponse object, you can just return the variable. Go back to the browser, refresh the page and notice the text displayed. It's important to know that this is just an example of how you can explore the HttpResponse object. In a real world scenario, developers do not usually need to modify the structure of the HttpResponse object.

To take this example further, you can also return the attributes of the HttpRequest object. For example, you can create variables to store the scheme, method, address, user agent and path info.

You may recall that the META tags provide information about the headers of the request object passed. One way to display the attributes of the HttpRequest object in the browser window. You need to render the variables inside a formatted string in Python, recall that to perform string formatting in Python, you use the formatted string literals, begin a string with the character f. Either in upper or lower case and place it before the quotation marks. Python expressions are placed between the curly braces.

To do this, add some HTML tags inside the formatted string and pass the variables that you created earlier.

This formatted string is then stored in a variable called message. Finally, use the return statement to return the HttpResponse object.

Notice that the message variable is passed as the first argument, now save the file, refresh your URL in the browser and notice that the request object information is displayed inside the browser.

A final thing to know is that you can update the header information for both the HttpRequest and response objects. To do this, create a HttpResponse object and then assign it to a variable called response, next type in response.headers and using a dictionary ad Age set to a value of 20.

Next, pass this value inside the formatted string, return to the browser and refresh the page.

Notice that the contents of the response header display with Age added as part of the header.

Developers use request and response objects when working with GET and POST methods. This is useful for creating forms, working with databases and other common data structures in Django.
'''