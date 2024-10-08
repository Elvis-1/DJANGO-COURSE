'''
When navigating the web, it's common to occasionally enter a URL or click a link only to find that the page that you are looking for cannot be found. In this video, you will learn how to handle errors and views using Django and explore how to create a custom 404 error page using the HTTP response not found class. Recall that Django displays a page not found error page when a URL cannot be matched. 


This default error page displays with some technical information for the developer, including the request method and request URL. However, you usually do not want your end-users to access this type of information, as these types of error messages will mean nothing to them.

Instead, you can create a custom view for the error page. Let's open up VS Code and explore how to work with error pages in views and switching the debug session from true to false. Let's begin by running a server first, by typing python3managed.py run server.

Next, open the local host URL in your browser and notice the default page loads. If you enter some URL, let's say home. Notice that a page not found error page is displayed by default. The page contains some error information and a message stating; you're seeing this error because you have DEBUG =True in the Django settings file. Change that to false, and Django will display a standard 404 page.

Debugging is the process of handling errors in code. In Django, debug mode is set to true by default, which displays detailed error pages during development. To apply this change, open the [inaudible] file under the my project and change the debug value to false

Additionally, you must add some value inside allowed host. In this example, add the star symbol to include all possible hosts. Save the file and refresh the webpage in the browser.

Notice that a different type of webpage is displayed stating not found. The requested resource was not found on the server. It's also possible to create a custom view for this error page. To do this, you must create a new file called views.py at the project level. Once created, open the URLs.py file and update the code with the necessary imports and URL patterns.

Additionally, you must add another URL pattern outside the URL patterns sequence. Next, create the view location, my project.views.handler404 and assign it to a variable called handler404. Next, go to the views.py file inside the project folder and import HTTP response. Create a view with the name handler404 as referenced previously. Inside the function, pass the request object and an exception argument. 

Then return the HTTP response object with some text value such as 404 call on Page not Found. Save the file and return to the browser and refresh the page. Notice that the message is displayed on the webpage. If you modify the URL with random values, the message remains the same. 

This is because the handler 404 handles all the pages not found by the URL configuration file. But if you add another view with a name defined in the URL configuration, notice that the view renders correctly. Similarly, just as the code uses the HTTP response object, you can also use HTTP response not found. Different classes in Django represent different status codes.

The HTTP response not found class represents status code 404 Page not Found. Modify the code in the function's return statement, save the file, and refresh the browser. While there is no visible change, the client receives the 404 status message internally. You can verify this from the browser's developer tools. Inspect the element by right-clicking on the mouse, go into the Network tab and clicking "Home". Once you refresh the page and click "Home" again, notice 404 not found. 

Often developers will modify the string to add some HTML elements, such as headings and a button. It's generally considered best practice to create a custom error page that's easy to understand, consistent with the website's branding, and directs users back to the homepage. In this video, you learned how to handle errors in views using Django. You also explored how to create a custom 404 error page using the HTTP response not found class.
'''