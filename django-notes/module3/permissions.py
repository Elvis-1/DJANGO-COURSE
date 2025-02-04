'''
In most apps, users are allocated different roles that allow them to perform certain actions. To enable these actions, they need to have the relevant permission granted to them. Think about the following scenario.

When you visit a restaurant, you're not allowed to go into the kitchen. However, if you are a member of staff, you are allowed to go into the kitchen. Web applications have a similar concept for controlling which users are allowed to do which action.

This is called permissions, and in this video, you will learn all about user, and model permissions in Django. The Django framework has an in-built system for handling permissions. This authentication system has features for both authentication and authorization, coupled for ease of use.

For a user to perform a certain action, they need to have the relevant permission granted to them. Before you explore permissions, it is important to note that a user in Django can be one of three classifications, namely a superuser, a staff user, or a user. Much like other components of Django, users in Django are Python objects.

The specific type of user is characterized by special attributes that are set inside the user object. Let me tell you more about the classifications. A super user is a top level user or administrator of the system. This type of user possesses permission to add, change, or delete other users, as well as perform operations on all the data in the project. 

A staff type user is allowed to access Django admin interface. However, a staff user doesn't automatically get the permission to create, read, update, and delete data in the Django admin, it must be given explicitly. Note that a super user is a staff user by default.

Everyone else is a regular user by default, a user is not authorized to use the admin site. Users are marked as active by default. A user may be marked as inactive if it's authentication fails or has been banned for some reason. While you can create the user through the admin interface, it can also be done through the Django shell. The permission mechanism is handled by the django.contrib.auth app. You can use the create user function to create a new user object.

Once the user is created, you can grant a certain status to a user to become a staff member. To grant the staff status, set the user is staff property to true. How do you create a superuser? Use a command directly inside the Django shell. When prompted, a password is assigned to this super user, followed by an authentication. Go to the admin interface and view the list of users.

The new user appears in the list. Remember that the superuser has every permission in the system, whether it is custom permissions or Django created permissions. There are several places where specific permission settings can be enabled, for example, to a specific model or object. How do you set permissions in a model?

As you create models in your Django application, Django automatically creates, add, change, and delete and view permissions. Permissions are named using the app action model pattern. App is the name of the Django app. Action is add, change, delete or view and model is the name of the model in lowercase.

Assume that a Django app called my app is created in the current project, and it has a model with the name my model declared in it. You can now apply your newly acquired knowledge. What will the permissions be? The permissions on this model will be as follows. Myapp.add_my model, myapp.change_my model, myapp.delete_my model. Lastly, myapp.view_ my model.

In Python code, it is possible to check if a user has a certain type or permission enabled on it. To do this, you can use the has_perm function, which returns true or false. For example, if the requesting user doesn't have the appropriate permissions, you can raise a permission denied error instead of returning the normal HTTP response. Assigning permissions to each user individually is a tedious task, especially if you have large numbers of users. Fortunately, Django has a solution.

You can manage permissions to sets of users in Django groups. That proves to be very useful. Now what is a group? In Django, a group is a list of permissions that can be assigned to one or more users. A user can belong to any number of groups. To go back to the restaurant example, you might have a group for kitchen staff and another group for waiters. When you create or modify a user, simply choose the desired group.

All the permissions listed in the group will be automatically assigned to the user. It is important to note that you can still manually add permissions to users, even if they belong to a group. In this video, you learned about the user permissions and model permissions in Django. You can give permissions to a user while creating it in the admin panel or from the shell interface. Using groups is a convenient way of enabling similar sets or permissions to multiple users. 

To enforce a permission while executing a view function, you can use the app permission required decorator.

'''

