'''
The basic workflow of any Linux command is that it takes an input and gives an output. The standard input device is the keyboard. The standard output device is the screen

With redirection, you can change the standard input and/or output. There are three types of IO or input/output redirections. Standard input, standard output, and standard error.

The shell keeps a reference of standard input, output, and error by a numbering system. The zero is for standard input, one is for standard output, and two is for standard error

Let's start with standard input. Taking input normally refers to a user typing information from the keyboard. We use the less than sign for user input.

The cat command can be used to record user input and save it to a file.

How do we take input and store it in a file such as a.TXT file?

Let me explain how you can do this by using an example to store user input to a text file. I have just launched my terminal, but how do we take input and store it in a file such as a.TXT file? One of the commands you learn to use frequently in this course is the cat command.

This command is actually set up to take in input.

On my terminal, I type the cat command, followed by a greater than sign, and then follow it by the name of the input file. In this scenario, input.txt, press Enter. Now I can add text to the text file created. At the end of the text, press Enter. Next, press Control D to tell the cat command that's the end of the file.

To output the contents of the file, enter cat, followed by a less than sign, followed by input.txt, press Enter. Notice that the text that I added from the keyboard displays.

Let's discuss standard output now.

A lot of the commands we have already used, for example, ls, send their output to a special file called the standard output. Output direction is handled with a greater than sign. IO allows us to use redirection to control where the output goes.

Now, I will demonstrate how you can send output to a text file. Everything in Unix, Linux is a file. This means every time you run a command like ls and press Enter, it sends the output of the file to an stdout file. In Linux, if you want to control where the output goes, you can use a redirection.
'''