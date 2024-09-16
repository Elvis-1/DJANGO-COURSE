'''
Remote refers to any other remote repository to which developers can push changes. This can be a centralized repository, such as one provided by Git hub or repositories on other developer devices.

The remote code is accessed through a URI which is unique and only accessible to those who have permission local.

Let's say we have a project called coding project one which is located on Git hub with a unique URL. 

In other words, this project is stored on a remote server. When a user wants to copy this project to their local device, they need to either perform a clone if it's the first time or pull it to get the latest changes.

 To clone a project a user must first choose a folder on their local machine. Coding project one is then cloned from the server and copied into the chosen folder. The user can then make changes to the project and push those changes back to the server.

First off, I'm going to create a new local repository using the Git in IT command.

I'll start by inputting M K D I R to create A new directory and then I'll set the name as my second repo. Next I'll use the change directory command which is CD followed by the name that I just said. Finally, I'll perform the Git in IT command to create my new repository.

If I execute another command called git remote, it comes back as blank. The reason for that is that I've only initialized a local repository which has no connection to a central repository that sits either on Git hub or another server.

Right now it's only available locally on my machine. Now I'll step back out from this directory and go into my first repo with a CD command. Again, this is a repository that I created earlier and does have a connection to Git hub. Using the remote URI I'll then check it by using the get remote minus V command. Git tells me that it's set to git tutorials 101 my first repo.Git. 

I'll step into the new directory once more using the CD command.

In this case we're going to add this URL to the remote settings by using the command. Git remote add specifying a name and then passing in URI, the name that is typically used here is origin. So I'll stick with that. So again the full command with the URL should read Git remote add origin Git at Github.com: Git tutorials 101/My first repo.Git. This time when I execute the Git remote minus V command. 

I have this set up against the get tutorials 101 which sits up on Git hub. What I'm going to do next is use the Git pull command which will connect with the GIT hub server, and pull down all the changes from the repository. So on my local I now have all the changes, but when I check the directory it's blank.

The reason for this is that I haven't set up a branch that matches with what I have on the server repository. Fortunately I can change that by performing the command. Git check out main

Which will set up a branch main on my local that tracks the branch main from the remote. And now when I check my folder using the LS command, it confirms that I have the read me test and test two files available on my local.


'''