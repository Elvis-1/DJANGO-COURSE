'''
The majority of web applications need to collect data
from end-users. This can be anything from user details for login
and authentication, registration details
for a new application or order details for
online shopping. Recall that web applications
use forms to collect data input from users
using HTML form tags. Any form elements such as
inputs are checkboxes, are sent to the server for processing when the
form is submitted.

In this video, you
will learn about forms in Django
and how developers use the form class
to automatically generate HTML for
elements from classes.

You will also learn how
developers can use models automatically generate forms to remove potential
processing errors. In Django, the most
common form submission is a post request, which will send the data
down in the post body.

The server-side code handles the incoming request and processes the data
on the backend. For example, suppose you create a basic form using
HTML to submit a name, you can use a label to display text describing what
the inputs should have. The input set to type text accepts input
from the end-user. In this example, the
inputs stores their name. The second input
of type submit is a button that displays
the text send name.

When the button is pressed, the action will be
triggered to make a post request to be
processed by the order view.

This is all defined in the form action and
form method attributes. While this process works well, the code can become tedious and complex when dealing
with large forms. For example, forums can have many different ways of gathering data with conditional flows. 

Also, designing forms in this
way can lead to errors as each form element's name or ID attribute needs to match what
the back-end code expects. To assist developers with
form creation and processing, Django uses a form class. In this class, you can define all the expected attributes that will be passed
down in the request. This means that you can use
a form class to represent the expected attributes and render the form
elements in the HTML.

For example, the soap bit name form can be represented
by creating a class. Let's step through this code line by line. First, you create a class called NameForm, which accepts a parameter of forms dot form. This is essentially
what is being passed in the form itself. Next, you create a
variable called your name, which is assigned forms dot CharField to represent the HTML input element.

Notice that you also can set some validation by setting the max length value to 100. Finally, When the name form class is rendered, it's rendered to a view
containing the HTML form code. It's important to know that the form tags are not represented. You need to add the
form tags and then use the templating to append
the form elements inside. Don't worry too much about
the concept of templating. You will learn about it soon. For developers, the advantage of creating forms in this way makes it much easier to manage any changes to the form.Instead of worrying about the names on inputs matching with
the server-side code, this is handled entirely
by the forum class. Also because you are
working with classes, you get all the benefits of
object oriented programming. For example, you can split complex forms into subclasses to make them more manageable. Unfortunately, learning about these features is outside
the scope of this video, but it's good to
know they exist. If you would like to learn more, there is an additional reading
at the end of this lesson. Lastly, let's explore the use of forms with
models in Django.

Sending data to
the back-end using the post method requires you
to persist the data somehow. For example, suppose
you are setting up a new user to gain
access to your site, you will need to persist their details such as
email and password and some general user information
such as name or address. Locally, developers can
solve this by using models. A model in your application will represent the table to
store this information. The model itself can then be used and be directly
converted into a Django form. This makes sense as
you want your forms to map to what you
need to persist.

This feature is excellent for ruling out any potential
issues or errors. The code for the model
form is placed in the file forms dot py and implements the
structure of the model, and you will learn more about both form types in more
detail later in this lesson. In this video, you
learned about forums in Django and how developers use the forum class to automatically generate HTML for
elements from classes.

You also learned how
developers can use models to automatically generate forms to remove potential
processing errors.


'''