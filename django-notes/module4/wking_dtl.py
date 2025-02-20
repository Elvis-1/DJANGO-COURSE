'''
A common requirement when creating web applications is the need to add dynamic data inside HTML markup. This data can be represented by a variable containing dynamic or calculated values or values stored in the database of the application. Either way, a web framework needs a way to understand this data. 


To address this, Django uses Django template language or DTL to separate the presentation and application logic. In this video, you will learn how to work with the Django template language. As you learned earlier, a Django template is a Python string or text document marked up using Django template language and interpreted by the template engine.

The DTL is based on the popular Jinja2 template engine, and has most of the features common to it. As a developer, writing code in a familiar language is beneficial. DTL helps remove that barrier by providing flexibility that aligns with the core time-saving principle in Django of do not repeat yourself or DRY.

It also adds a layer of security as the Python interpreter does not execute the template code. Once you understand the use of template languages, much of the logic in creating the templates becomes evident. There are four main constructs in the syntax of DTL. They are variables, tags, filters, and comments. Combined, they provide the substitute for basic functionalities present in a programming language. Let's explore each one now in a little more detail starting with variables.

Variables are surrounded by double curly braces. When the template engine encounters a variable, it evaluates that variable and replaces it with the result. Variables return a dictionary-like object that maps keys to values.

In this example, restaurant name is the key with the value of Little Lemon. When rendered, this template code displays Welcome to Little Lemon restaurant. Similarly, you can use dictionary, attribute, and list index lookup using.notation.

Now you know about variables. Let's move on to tags. Tags are the source of logic that you can add to templates. Tags are created using curly braces and the percentage symbol. The most commonly used tags are the control structures such as if and for loops. The if tag is used inside the template to render different outputs.

A typical use case is to check the login status of a user. The code in this example checks if the value of the Boolean variable logged in is true or false. If true, the page renders the welcome statement. If false, it renders the login link.

Another standard workflow is to iterate over the dictionary to display an unordered list. To do this using a template, you need to have some way of looping over the data and printing out the HTML markup with the data object for each item in the list. Let's now understand how a template list with a for loop works. For example, suppose you have a simple list that contains menu items for the restaurant.

Each item has a name and a price. To create this menu statically, you wrap each menu item in an unordered list using the list item tag. To create this Menu dynamically with templates, you add the for loop code where items repeat. In this menu example, it's inside the unordered list. The code will iterate over the menu list object and display the name and price.

The variable item will keep a reference to each object as the iteration continues to go through each menu item. Apart from if and for, there are many other texts such as extends and include, and you will learn about them later in this lesson. Now, let's explore filters. Unlike tags, filters can change the values of the variables.

For example, if you add a filter such as string upper, it will take an input string and convert it to uppercase. Filters can also additionally take an argument like when using the date filter. For example, you can pass the argument for year, month, and day, which produces a date in this exact format. 

Finally, let's explore comments. You can create comments using the curly brace and percentage symbols. Django ignores everything in-between the two tags. It's important to note that developers use comments for documentation as they do not render. 

In this video, you learned how to use the Django template language. Developers frequently use tags and filters when working with DTL to create dynamic data, and you can learn more about them from the link in the additional reading at the end of this lesson.
'''