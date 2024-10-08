"""
Have you ever noticed the lock icon beside the URL in your web browser? This means that HTTPS, the secure version of HTTP, is being used. HTTP is a core operational protocol of the world wide web. 

It is what enables your web browser to communicate with a web server that hosts a website. Most of the time, HTTP is the communication protocol you use to browse the web

HTTP stands for Hypertext Transfer Protocol. It is a protocol used while transferring web resources such as HTML documents, images, styles, and other files. HTTP is a request response-based protocol.

A web browser or client sends an HTTP request to a server and the web server sends the HTTP response back to the browser. Next, let's explore the makeup of a HTTP request. A HTTP request consists of a method, path, version, and headers.

HTTP method describes the type of action that the client wants to perform and it communicates it to the server. The primary or the most commonly used HTTP methods are GET, POST, PUT, and DELETE. The GET method is used to retrieve information from the given server.

The POST request is used to send data to the server. The PUT method updates whatever currently exists on the web server with something else and the DELETE method removes the resource. The path is the representation of where the resource is stored on the web server.

For example, if you wanted to request an image from a page in a website, then the URL in the address bar would need to contain the full path to that particular file on the web server. There are multiple versions of the HTTP protocol. You want to explore these right now, but be aware that versions 1.1 and 2.0 are the most used.

Finally, there are the headers. Headers contain additional information about the request and the client that is making the request. Headers can contain information such as the server name, the server port, the request method type, and the content type. 

The contents of the header can depend on the specific client and server, but these are some of the most common. For certain request methods, the request will also contain a body of content that the client is sending. Now, let's cover some details about the makeup of HTTP response. HTTP responses follow a format similar to the request format.

Following the header, the response will optionally contain a message body consisting of the response content, such as the HTML document, the image file, and so forth. HTTP status codes contained within the header indicate if the HTTP request successfully completed. The code values are in the range of 100-599 and are grouped by purpose.

The status message is a text representation of the status code. During your web browsing, have you ever encountered pages that display 404 error not found or 500 errors servers not responding? Let's explore these HTTP status codes briefly and explain about their grouping. There are five groups of status codes.

They are grouped by the first stages of the error number. Informational is grouped from 100-199, successful responses are from 200-299, redirection messages are from 300-399, client error responses range from 400-499, and server error responses are 500-599. Informational responses are provisional responses sent by the server. These responses are interim before the actual response.

The most common informational response is 100, CONTINUE, which indicates that the web client should continue the request or ignore the response if the request is already finished. Successful responses indicate that the request was successfully processed by the web server, with the most common success response being 200 OK. You're receiving these responses every day when you receive contents successfully from a website. The meaning of OK depends on the HTTP method.

If the method is GET it means that the resource was found and is included in the body of the HTTP response, if it's POST it means the resource was successfully transmitted to the web server, and if it's PUT the resource was successfully transmitted to the web server. 

Finally, if the method is DELETE, it means the resource was deleted. Redirection responses indicate to the web client that the requested resource has been moved to a different path. 

The most common response codes used are 301 Moved Permanently and 302 Found. The difference between the redirection messages through 301 and 302 is that 302 indicates a temporary redirection, the resource has been temporarily moved.

When web browsers receive these responses, they will automatically submit the request for the resource at the new path. Client error responses indicate that the request contained bad syntax or content or cannot be processed by the web server. Let's explore some of the most common response codes. 400 is used when the web browser or client submitted bad data to the web server.

401 is used to indicate that the user must log into an account before the request can be processed. 403 is used to indicate that the request was valid but that the web server is refusing to process it. This is often used to indicate that a user does not have sufficient permissions to execute an action in a web application. 404 is used to indicate that the request resource was not found on the web server. Server error responses indicate that a failure occurred on the web server while trying to process the request.


The most common code used is 500 internal server error, which is a generic error status indicating that the server failed to process the request. Have you ever bought something online and needed to enter your credit card information? You wouldn't want someone else to get this information from the HTTP request. This is where HTTPS must be used. HTTPS is the secure version of HTTP. It is used for secure communication between two computers so that nobody else can see the information being sent and received. It does this by using something called encryption.

You won't cover encryption right now. Like in HTTP, the requests and responses still behave the same way and to have the same content. The big difference is that before the content is sent, it is turned into a secret code. Only the other computer can turn the secret code back into its original content. 


If someone else was to look at the code, it wouldn't be understandable. You use HTTPS every day. This is the lock icon that you see beside the URL into your web browser. Before I finish, I want to leave you with a brief summary of HTTP. 

Firstly, it is a protocol used by web clients and web servers. It works to transfer web resources such as HTML files and is the foundation of any data exchanges on the web. Also, remember that by using HTTPS, we send the information securely. Requests are sent by the client, usually a web browser, and the server replies with responses which may be the return of an image, our HTML page. HTTP requests have syntax that includes, method, path, version, and headers. HTTP responses follow a similar format to the request. An HTTP status codes indicates whether the HTTP request successfully completed. The status code is a three-digit number that corresponds with groups representing different types of results. Well, now you know how the HTTP protocol request and response cycle works. You know about its methods and the elements that make up a HTTP request. Good job.
"""