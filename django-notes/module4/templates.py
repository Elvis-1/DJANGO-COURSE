'''
Web frameworks often need to generate dynamic content to render on web pages. And because Django is a web framework, it provides a convenient way to generate HTML dynamically. Dynamic content is any data that changes according to context, user behavior, and preferences. Developers can use dynamic content and rendering to produce static HTML code. The most common approach for developers is to use templates. In this video, you will learn how to use templates in Django

You will also explore the concept of the Django template engine and the Django template language. Templates are text-based documents or Python strings marked up using the Django template language, or DTL for short. Templates consist mainly of two types of content. The first is static. This is the HTML that does not change on the web page.

The second is template language. This is the syntax that allows you to insert dynamic data. Let's explore an example of creating a HTML heading element using dynamic content.

In this example, the variables dish_name and price are placed within the double curly braces. These variables represent dynamic content.

The remaining content, including the HTML heading tags, is static. It's important to understand that the static part defines the structure and layout of the page and a view using the render function handles the processing of the dynamic content.

You may recall that the render function takes three parameters, request, path, and a dictionary of variables. When you pass the dictionary object to the render function, the process of rendering replaces variables present with their values which are looked up in the context. While you use template language to render dynamic content, the concept of a template is what makes up the presentation layer of the MVT architecture.

This helps in the separation of logic because templates handle the user interface logic of a web page. It's important to know that the dynamic content inside the static HTML is written so Django can understand the syntax and formatting. Python is a dynamic object-oriented programming language, while HTML is a static markup language.

To bridge this gap, Django makes use of the Django template engine. And the Django template language, or DTL, is the language used for adding dynamic content. DTL can contain embedded dynamic content, such as Python code and variables that the template engine processes.

DTL consists of constructs such as variables, tags, filters, and comments. Each construct has a specific syntax that helps Django understand the code logic. For example, you can use tags and comments to build a for loop to display list item elements. The tags map the dictionary values from the context and helps to add logic to the template. You will learn more about each of these later in the lesson.

Additionally, Django also provides an API for loading and rendering templates. You define the configuration settings for the template engine inside settings.pi under the project directory. It's important to note that the app directory setting must be set to true. This setting tells Django where to search for templates. For example, search inside a subdirectory named templates for each application in the project.

You can also add specific locations inside the directory setting for Django to search for directories inside the DIRS option. In addition to the Django template engine provided by Django, you can also extend the functionality by using one or more template engines. For example, Jinja2 is a popular template engine used in Python and you can configure the settings for adding these extensions inside the settings.pi file.

For example, you can change the default environment settings for Django to use Jinja2. Okay, so now you know about template engines, let's explore the concept of code reuse.


Django helps in code reuse by using templates with the help of something called template inheritance. Template inheritance allows developers to build a base template containing the expected HTML elements of your site and defines blocks that child templates can override. Once defined, all pages of the website can inherit the base template. This code reusability helps in saving developers time and effort and follows the principle of dry.

For example, you can create a base template containing the HTML code for your site's head, body, and main sections. Then, in a child web page, you inherit the base template and place the specific content of the page. It's a standard best practice to place template files inside a template folder. In this video, you learned how to use templates in Django.

You also explored the concept of the Django template engine and the Django template language. Templates are quite a vast topic in Django, and you will learn more about them for the remainder of this lesson.
'''