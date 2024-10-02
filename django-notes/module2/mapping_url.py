'''
Previously, you learned that to define URLs, you first define the URL structure using the path function and then this URL is mapped to a view function. Sometimes developers need to pass information to the view function for additional processing. 

In Django, developers have the option to pass values as URL parameters by using URLs as source of information. In this video, you will learn how to use URL parameters to retrieve data from a URL and send it to the view function for processing. You will also explore how to use angle brackets and path converters to capture a parameter value from the URL.

Suppose the owners of Little Lemon want to add a web page to display a name from the drinks menu. The name is sent in the URL and then displayed as a heading on the page. For example, the URL can contain the names of coffees like americano espresso and cappuccino. 

The last part of the URL represents a drink name and this value can be passed to the view function from the URL as a parameter. In Django, you can capture a value from a URL using angle brackets inside the path function where you define the URL. Captured values can optionally include something known as a converter type.

You will learn more about this later. For now, just know that to capture a string you can use the keyword STR followed by name for the value. Then inside the views.pi file you pass this name as an argument after the request object. Let's open VS code now and create a food item page by configuring a URL and passing a parameter to the view function. 

First, open the URLs.pi file. And inside the URL patterns list at a path. Inside the path function defined the URL as dishes forward slash. And then inside angle brackets place the path converter for a string. The example in this video is str colon and then dishes. 

Next, add the view functions location views.menu items. STR represents the path converter type and dish is the URL parameter name given to match the value. For example, if the URL parameter contains the string, pasta, it will be represented as dish equals pasta. Once this code is complete, open the views.pi file and create the view function. First, make sure to import the http response object.

This function will match the path defined inside the URLs.pi file. In the function declaration, you need to pass an additional argument after request because an argument was passed inside the URL.pi file. Inside the function body, create a dictionary called items.

Once the dictionary is set up, add some entries to it. In this example noticed that three key value pairs were added with the keys of pasta, falafel, and cheesecake. Next create the code to access the dictionary by passing a value and save it to a variable named description. The logic of this code is that the URL parameter value passed to this function will be matched to a key inside the dictionary.

Then the associated value is stored in the variable named description. The final step is to return the http response object containing a html heading to display the function argument and the associated description variable as plain text. Save the code and run the server. Open the browser and add dishes forward slash pasta at the end of the local host URL. 

Remember that the word pasta is one of the dictionary items. The text displays in the browser, formatted with the URL parameter as a heading and the dictionary description as text. Similarly, if we modified this to let's say cheesecake and press enter, notice the text updates accordingly. Defining URLs with parameters has a wide variety of uses. In this example, the logic of the view function was to pass a URL parameter that matches the description in a dictionary. Developers can also use URL parameters to send information to the logic layer for processing or as search and sorting criteria.

Similarly, URL parameters can be used to fetch data that can be used with forms, data models, and other data structures. For example, you can use a URL parameter to pass the primary key of a database table using the INT path convert type.

Once the primary key is sent to the view function, it can fetch the database row and its data. And you will learn how to do this later when you explore jangle models. Mapping URLs with parameters is also useful to create meaningful grouping of the content. In this video, you learned how to use URL parameters to retrieve data from a URL and send it to the view function for processing.

You also explored how to use angle brackets and path converters to capture a parameter value from the URL.


'''