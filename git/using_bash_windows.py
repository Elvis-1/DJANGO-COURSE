'''
Let's navigate to my home directory.

I type the CD command and then a tilde(~), followed by the Enter key. Then I use the LS-LA command to return all of the files in a list including all hidden files.

Notice two files, a bashRC file and a bash profile file. For now, I want you to focus on the bash RC file first.

I can use the command les.bashRC to check this file. The bashRC file is mainly for configurations. It is essentially a script file that's executed when you first open the terminal window

The bashRC file is mainly for configurations. It is essentially a script file that's executed when you first open the terminal window. What's in there will be configurations for the shell itself, for example, the types of colors that I'm using. I can also add in things around my shell history, like how much history of previous commands I want to store and so on. Any configuration options that I put in here will be executed when the terminal session begins. I press the Q key to exit the less environment

The other file is the bash profile file. I can run the less command again, this time with.profile. This tends to be used more for environment variables. For example, I can use it for setting environment variables for my Java home directory or my Python home directory or whatever is needed during development. Again, I press the Q key to exit.


Now, I will create a simple shell script. For this example, I will use Vim, which is an editor that I can use which accepts input.

Type Vim and then I create a new file by typing the test shell.sh and press the Enter key. Then at the top of the file, I put in what type of file I want it to be. In this case, it's going to be a bash file. If I press the I key on my keyboard, it'll set insert mode. Then I put in a hash symbol followed by an exclamation mark, a forward slash, the word bin, another forward slash and then the word bash. This let's to the operating system know that this is a bash script


This script is very simple. I want to print out some type of text onto the screen.

 I use the echo command and type in what I want to print out. In this case, HelloWorld, press "Escape" to get out of insert mode. Then I type:wq! to save the file. 

 Press "Enter". If I look in the directories now, notice there's now a file named testshell.sh

 The other thing to notice is that this file can't be run at the moment. In other words, it's not executable.

 It's just a read write file. But I want it to be executable, which requires that I have an x being set on it.

In order to do that, I have to use another command which is called chmod. After using this command, I type in the type of permissions that I want. I type in 755. Then I want to set the file that I want to add the permissions to, which is testshell.sh. If I use the LS-LA command again, I notice that the file has now been turned into an executable file. This means that I can now run the file from the command line. To run the file, I press./testshell.sh followed by the Enter key. Now you notice the words hello world are printed out on the screen

This is how you can create simple scripts and make them executable within the bash shell.

'''