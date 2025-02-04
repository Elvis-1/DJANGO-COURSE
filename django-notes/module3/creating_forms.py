'''
By now you should be familiar with the concept that developers use the form class, to automatically generate HTML for form elements from classes. In this video you will learn how to create a form using the form class in Django.

You will also learn how to render a form using a template.

Finally, you'll explore some of Django's form features such as validation. Let's begin creating the form. First I need to create a file called forms.py inside the app directory. In this scenario I will create a form on the little lemon website that allows the employees to log their entry times of work. In this video I will be only demonstrating how to build the form using the forms API and Django.

You'll learn how to process forms and Django later in this course. The process of building forms in Django is very similar to creating models. First I use the import statement to import forms from the Django module. Next I create a class called input form, which will hold the form and pass it forms.Form.


This class needs four attributes. The first two attributes are first name and last name, which will be character fields with a max length set to 200. The third attribute is shift which will be a choice field. It will let employees choose between morning, afternoon and evening shifts for their work. Inside the choice field I pass the choices as one constant called shifts.

Then at the top of the code I assign the value of this constant to an iterable of tuples inside a tuple. I need to add one final attribute called time log. This attribute will log the entry time for a given employee. I type forms.TimeField. My code looks good and that's all I require for creating a form. 

Let me now switch to the views.py file and just like I did with models I need to create a view for this form. I do this with the import statement to import the form from the app directory. Now I'm ready to create a view. First I create a view function called form view. Next I create an instance of a form and pass it to a variable called form.

Then I create another variable called context which is assigned to a dictionary with form as the key, and the instance object of input form as its value. Finally I pass this variable inside of the render function which will display the output of an HTML page called home.html. 


But for this to work I must build a webpage by creating a template. I first create a templates folder inside the app. Next I create a home.html file and paste the HTML code inside of it. It's important to remember to use the form method of post as I'm sending the data from the form and creating an object from it. I've also included a submit button represented by an input field with type and value set to submit.

To finish this form code I have to add something called a CSRF token, which is simply a way of telling Django that the form data is safe. Finally I pass the form that I've created. My code looks good let me save all my files, and before I continue I ensure I update the URLs.py file, both inside the app and the project folder. I also need to update the settings.py file with a reference for the app.

I'm now ready to run the server. In the terminal I type the command python manage.py runserver. I navigate to localhost URL and enter the path for the form. Success. The form displays on the webpage with the form elements first name, last name, shift, and time log. You may notice that the form does not have any styling applied. 

Well I could use some CSS, I'm not going to just yet. Instead I want to demonstrate a trick to structure the form elements using paragraph tags. Back in the file home.html I can modify how the form is rendered by amending the form to form.as_p. This will tell Django to render the form elements as paragraph tags.

Save this file again and refresh the web page. Notice that the form elements all appear one after another. When I press the submit button, notice that Django also provides basic form validation where all the elements are required. If I want to change this I can pass a parameter inside the forms file. For each attribute I can type required equals false.

I saved the file again and refresh the web page. I press submit and notice that the field first name is not required at this time. Similarly I can pass other parameters. For example inside the time log I can type help text equals and then the text enter the exact time. Once again I save and refresh and notice the text is displayed beside the time log field. 

Finally I can open my HTML file to add some inline styling to the form. Inside the form declaration I add a background color. I save the file one more time and refresh it. Notice that the form displays with the background color. Working with forms can be complex, so developers can use Djangos formed functionality to simplify and automate vast portions of this work. 

By creating forms this way, developers are guaranteed to add Django's layer of security. It was not possible to demonstrate how to process and save the form in this video, but I hope you're thinking that maybe Django offers similar functionality to process and save forms as it does with creating them. If you're thinking that you're correct, and you will learn how to do this soon.

In this video you learned how to create a form using the form class in Django. You also learned how to render a form using a template. Finally you explored some of Django's form features such as validation.
'''