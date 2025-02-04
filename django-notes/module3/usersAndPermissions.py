'''
You may remember that you can create different types of users in Django. Now you will explore how to add and remove permissions for these users. The Django framework has a built in mechanism that manages permissions quite efficiently.

The Django admin web interface makes it easier for you to create and modify users or user groups. You can also grant or revoke permissions for individuals and user groups.

While Django admin has a user friendly interface which makes handling permissions quite easy. It is also possible to handle permissions through the Django shell. To demonstrate this, let's first create a user and then locate the required user by its user name.

To do this, you must first open the interactive Django shell that has Django settings already imported. It allows you to directly work with the root project folder. Next import the user module from the specific django.contrib package. Then define a variable and assign it to create user method.

And pass the arguments for user name, email, and password in that order. Once the user is created to find another variable and assign it the get method of the user object then past the user name as the argument. Once the user is created, the next step is to assign permissions.

Django comes with a built-in permission system. It provides a way to assign permissions to specific users and groups of users. When django.contrib.org is listed in your installed apps setting, it will ensure that four default permissions are available. This functionality allows you to add, change, delete, and view permissions.

And are created for each Django model defined in one of your installed applications. Permissions can be set not only per type of object, but also per specific object instance. By using the methods provided by the model admin class, it is possible to customize permissions for different object instances of the same type. 


Similar to the admin permissions you learned about, permission specific to models can also be managed using the model admin class. The model admin class methods include view, add, change, and delete and are used to customize the permissions. Now that you have learned about the concept of permission using the Django shell. Next let's explore user objects. 

User objects have two main fields known as groups and user permissions. User permissions store and reference a single or multiple permission objects. Permissions can be granted or removed by calling the methods set, add, remove, and clear on the user object. 

Let's explore an example using the add method to grant permissions to the user Mario. In this scenario, let's provide one or more permission objects. You use the add method to add a permission to change the menu model inside the app myapp. It's important to know that once you add django.contrib.org to the installed apps list, you must run the migrate command to implement the change. Note that when you run manage.py migrate each Django model is assigned the default permissions. 

For example, suppose you have a Django app called myapp in which there is a model named mymodel. If you run boolean expression to verify the permissions to add, change, delete, and view, they will return true. In addition to the default permissions, custom permissions can be declared in the models meta class, which can be declared inside the model. So far you have covered how you can modify permissions on the Django shell.

However, in practice it is much easier to deal with them using the Django admin interface in the browser. Let's explore how you can add and remove permissions using the Django admin interface. Building on the earlier example of adding groups and users, let's explore how to assign permissions to different users using the Django admin panel. In the browser at the admin login page, let's enter the credentials for the existing super user.

Once you log into the admin panel notice that you have choices for groups and users. In the authentication and authorization section, click on the link for groups. The first thing to know is that you can create groups in addition to the existing staff group. 

For example, let's say you want to add some more groups. The first is for the reservation desk staff and the second is for the little lemon website administrators. Click on the add group button and a new page with a form to add a group loads. You must give the group a name. In this example the name will be reservation desk. Inside the permission section, notice that you have several options in the available permissions table.

Let's say you want to assign this group permissions for the reservations model. You can select the reservation permissions to add, change, delete or view reservations. Then click the choose button to add the permissions to the chosen permissions table. Once transferred, click the save and add another button to create the group for the website administrators. 

Notice that the add group form resets allowing you to add another group. Create a new group called admin users but this time assign all the permissions by clicking the choose all button. As all the groups are created, you can click the save button. Okay? So now that the groups are created, the next step is to add the users. In the authentication and authorization section, click the user's link to open the user's page. Suppose you want to create a user called Mario inside this section.

Remember Mario is the owner of Little Lemon. Click the add user button to load a new web page that displays an ad user form. To add a new user, you must enter the login credentials. So enter Mario as the user name and then set a password. Click the save and add another button to add a new user. The second user is Maher a staff member at Little Lemon. Assign a password and click the save button.

Notice that when you click the save button Django administration immediately takes you to the page where you can assign additional information to the user you just created. There is a personal info section where you can add the user's first name, last name, and email address. In the permission section, you can change the permission level and assign the user to a group. In this example the user Maher is a staff member.

So let's keep the permission as active and also assigned the permission of staff status. Next assign Maher to be part of the reservation desk group. It's important to know that once you assign a user to a specific group, all the permissions that are entitled to the group get automatically assigned to the user. 

And it's also possible to assign additional user permissions. When you finish assigning a group and permissions to a user, press the save button. Next it's time to add a group and permissions to the user Mario by clicking on the user's name in the user's table. First enter the personal info for the user Mario. Next assign him the status of super user. Make him a part of the admin group and save the changes to return to the user's page. 

It's also possible to filter the users by different categories. In the filter panel, you can filter by the staff status, super user status or the status of the groups in which they are assigned such as admin users. Finally, on the main home page notice your recent actions display in that recent action section. 

This feature allows you to configure different users quickly and set their permission levels. In this video, you had an introduction of how to handle user permissions from the Django shell. You also covered a demonstration of how to add groups, users, and modify permissions using the Django admin interface. Good work.
'''