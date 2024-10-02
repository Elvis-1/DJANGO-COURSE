'''
By now, you should be familiar with the concept of mapping URLs with parameters in django.

Django lets you design URLs however you want, and you do this by using the path function and path converters. For example, creating a custom URL with dynamic values for more complex matching requirements, you can define your own path converters using something called regular expressions.

In this video, you will learn how to use regular expressions to define URL patterns in django. Suppose you have been tasked to create a menu item page for the Little Lemon website. The page displays content for each item on the menu. Instead of making a specific page for each menu item, you can define the dynamic URL structure that will pass the menu item ID to the view function.

The content of the page will depend on the menu item value pasta to the view function from the URL. Based on the ID value pasta in the URL, the logic in the view function will determine what type of data to display, like a menu item name.

The advantage for developers is that they only need to create one page. Instead of creating individual static pages for each menu item, developers only need to create one page whose content updates dynamically based on the values pasta in the URL.

However, to ensure that the URLs structured in the way that the view function requires, you need a way to define and verify the values and format of the URL. To verify that the Euro values pasta to the view function are correct, you can use regular expressions. Regular expressions are RegEx, are a set of characters that specify a pattern and are used to search for or find patterns in a string.

They are a powerful tool that developers use to perform extraction and validation, advanced searching, group searches, and find and replace operations. In django, developers use regular expressions to define, extract and validate dynamic URL paths before they are sent to the associated view function.

This video focuses on using regular expressions in Django URL paths. However, it's important to know that regular expressions are not specific to python or Django. They have many uses across various areas of computer programming and software development. Regular expressions and their associated characters are universal, meaning they are the same across all programming languages.

Let's begin by exploring an example of a URL pattern containing two entries in the urlpyfile. The first path is constructed using a regular URL, and the second with a regular expression path. Let's step through the code line by line.

First, you import two functions, path and regular expression path from the django.urlsmodule. Regular expression path is used for paths that need to contain a regular expression, inside the URL pattern sequence there are two entries. 

This example will only explore the first argument pasta inside these functions. Notice that the first path contains the URL string of menu item forward/10. This string is static and immutable, which means it has no possible numerical variations even if in the same format.

For example if you enter a URL such as menu item forward/1, it will not match this path and map to the view. As a result a 404 not found error message will be displayed. You can accept all URLs in this format using the regular expression path function like in the second entry. 

Notice the character r at the beginning, this makes a row string which treats the back slashes symbols as literal characters and not escape characters. Let's explore some of the most common symbols used. First is the caret symbol used as the anchor at the start of the string, it can also be used for negation. 

Next is the dollar symbol which is used as the anchor for the end of the string. You use opening and closing square brackets to define a character set that matches any one of the characters present inside.

Next, opening and closing curly brackets are used to specify the exact number of proceeding characters. 

Finally opening and closing parenthesis are used for grouping parts of the RegEx. Now that you are familiar with some of the characters, you can use them in regular expressions. Let's revisit the URLs structure from the little lemon menu example.

The URL begins with a string with the word menu item, then it's followed by a forward slash, followed by parenthesis for grouping. Inside the parenthesis exists two occurrences of numbers between 0- 9. Outside the parenthesis is another forward slash, followed by the dollar symbol to end the string. Acceptable strings for this RegEx can be menu item forward slash followed by the range 1 to 99.

Regular expressions are extremely useful while creating you URLs, but at the same time they can often get complex. And this is especially true for regular expressions containing several special characters. It's common for aspiring developers to feel confused when first learning regular expressions. Sometimes a symbol can be used for one or more purposes or the same symbol can behave differently depending on the case.

Getting familiar with their usage requires some practice and a little patience. It's advisable to start with the example in this video and build your knowledge using the remaining readings and exercises in this lesson. In this video, you learned about regular expressions and how developers use them to create and validate dynamic URL in Django. If you would like to learn more about regular expressions, there is a link in the additional reading at the end of this lesson.
'''