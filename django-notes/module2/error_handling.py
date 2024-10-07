'''
an application will contain errors in some form no matter how much testing or QA is performed. This is not always directly related to incorrect code or syntax issues By their very nature networks are not always 100% reliable and things can occasionally go wrong as an aspiring developer.

You need ways to handle these potential issues in this video. You will learn about error handling in Django. You will explore some of the most common client and server error responses that developers encounter and you will also learn how to work with them in jangle via the air handling view. 

By now, you should know that http responses contains status codes recalled that the 100 are used for informational to hundreds referred to success. Three hundred's for redirects are moved resources. 

Four hundred's for bad requests or authorization issues and the five hundred's for server issues. While this may seem like a lot of codes to learn, you generally encounter some of the same codes more frequently.

When working with web applications. Let's explore some of the more common client and service status codes that developers encounter starting with client or response codes.

The first is 400 which represents a bad request. This occurs when parameters passed in the request are not what the server may expect. Next is 401, which indicates that the user must log into an account before processing the request. Next is 403 indicating that the request was valid but that the Web server refuses to process it.

This typically means that the user calling the resource does not have the required permissions to view the resource. Finally, 404 indicates that the requested resource was not found on the web server. This typically happens when the resource cannot be located at the specified file path. Now that you know some common client error responses, let's explore some server error responses. Server or responses usually indicate a failure occurred on the web server while trying to process the request. This can mean many things. For example, the application has failed or is not running or the time limit on the calling request may have aborted due to the server taking a long time to respond Server or responses usually use status codes ranging from 500 to 599. The most common code you will likely encounter is the 500 internal server error which is a generic error status indicating that the server failed to process the request. Okay, Now that you have learned about the error response, let's now explore how Django handles them. By raising exceptions.

Django handles all our cases by raising an exception which is invoked via an error handling view that you can configure. These are handling views are added to a separate views. That pie file that must be created at the project level to get applied across the project. The views to use for these cases are specified by four variables. 

They are handler 400. Handler 403. Handler 404 and handler 500. It's important to know that while you can use the default values and views for your projects, there may be times when you want to customize the look of these views to align with the style or theme of your site. Further customization is possible by overriding the default values. 

Such values can be set in the root U R L configuration file of your project. It's important to know that setting these variables in any other U R L configuration file will have no effect. Let's explore these variables in a little more detail now to override their defaults and implement some custom views.

The first is handler 400 by default. This is the bad request view. Next is handler 403 by default. This is the permission denied view Next is Handler 404 by default. This is the page not found view finally, handler 500 by default. This is the server or view. As you have learned. It's also possible to implement custom views and you will learn how to do this soon for now.

Just know that to implement a custom view. The view function needs to accept the appropriate request argument and return the appropriate response. The custom views that you create using these handlers return different http response sub classes that handle different types of http responses for example class. 

Http response Not found. Acts just like http response but uses a 404 status code class http response. Bad request acts just like http response, but uses a 400 status code class, http response forbidden acts just like http response, but uses a 43 status code class. Http response. 

Server error acts just like http response, but uses a 500 status code. In this video, You learned about error handling in Django.
'''