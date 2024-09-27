'''
In this video, you'll learn how to create view functions that return text and HTML markup using the HTTP response object. Then you'll learn how to map these functions to URLs so that they can be displayed to the end-user in a web browser.


By now, you should be familiar with the concept of views and how they're used to create view functions with the logic and the views.py file. I've already created an app inside the project and the first thing I want to do is return the text Hello World on a webpage. 


First I open the file called views.py and paste in some code. Notice the HTTP response that I imported on line too it allows me to communicate with the server. In this video, when referencing the server, I will often use the words request and response.

Recall that requests refers to requesting information from the server via a code and response just means that I'm returning an HTTP response to the server, then the response is displayed on the webpage. It's important to know that when I create a view function that returns an HTTP response, it won't do anything on its own. This is because Django doesn't know where to return the content Hello World

To make this work, I need to map the view function to a URL using the URL configuration file called URLs.py in the project directory. Let me open this file and add a new path. Once I add the path, I need to import the views.py file from my app directory. Now Django can access the views file and the hello function that I've defined.

Notice that the path contains the URL and the name of the function from the views.py file that I want to map to. The first argument that's passed to the path function is the URL location that's added as a suffix to the URL or local host. If this doesn't make sense at the moment it will when I preview the webpage in the browser. Now, I run the server by typing the command python managed.py runs server.


I can open the development server by clicking the URL for the local host or copy and paste in the browser. Notice that 404 page not found error is returned. The reason for this is because they added the path of say hello to the URL so I need to add that now as a suffix. Now when I press Enter, notice that our webpage is displayed with the text Hello World

Now I want to create another view function inside the app. So back in the views.py file, I create a new function called homepage. This returns the text, welcome to little lemon. Once again, to map this view function to a URL, I opened the URLs.py file and add a path that will access the views.homepage function. Notice how I've added a new location called homepage to retrieve the content and this will reflect in the new URL

I save these two files and returned to the web browser. I change the suffix from say hello to homepage. Press Enter, and notice that the new output is displayed. You may be wondering how does all this code integrate with Python? Let me demonstrate this by adding a third view function that accesses the datetime module in Python, then I need to make sure that I import the datetime module so my code has excess.

That looks good to me. Now my code has access to the year that uses the datetime module. It's stored in a variable named date_joined. Notice that this value is returned to a webpage and to map it to a URL, I once again open the URLs.py file to add the associated path. Once again, I save the files. Now when I visit the webpage, I can access the URL with the suffix display date. This displays the year. I'm happy with the code so far. However, there is one last view function left for me to add.

Back in views.py, I add another function called menu. This code allows me to pass HTML code inside an object in Python, and I can return that object as an HTTP response. Notice that I've also added some styling by changing the color of the code. I save my file and once again create the path. It's important to remember to always save the file is after every update. 

 Now let me revisit the webpage again and go to the URL I've created. Notice that the text displays with HTML markup and some CSS styling. In this video, you learned how to create view functions that return the text and HTML markup using the HTTP response object. Then you learn how to map these functions to URL so that they can be displayed to the end-user in a web browser. Well, at the moment the content return is basic.

 
'''