'''
Grep stands for global regular expression print.

And it's used for searching across files and folders as well as the contents of files.

On my local machine, I enter the command ls -l, and see that there's a file called names.txt. If I access that file using the lass command, it displays a list of first names in non sequential order, as in, not arranged alphabetically

So what I'll do first is use Grep to find some patterns of names that start with similar matches

First I'll perform a standard search using Grep. So what I'm going to do is look for names that begin with Sam, by entering the command, grep Sam names.txt.

Keep in mind that Grep is case sensitive, which means if I run the same query with a lower case S, it returns a completely different set of results.

Fortunately I can pass in a flag to ignore case sensitivity. I can do this with a command, grep -i, followed by the keyword Sam. And then the file name names.txt again. This time I get back both users that begin with Sam and also with Sam as a partial match in the middle or the end of the name

We could also do an exact match by passing in a different flag, and that's the dash W. Which means it'll match exactly what I'm looking for. So I'll input, grep -w, and then pass in the key word Sam, with a capital S, and finally our file name names.txt

Lastly, I can use a pipe command to combine different searches for Grep itself. For example, let's say I went to search across a list of directories for certain, executable files. I can combine that with different commands and search across the file structure to find exactly what I'm looking for. If I check all the executable files inside the bin directory by running, ls /bin, it returns a long list of results. In order to filter that down, I can run the same query of ls /bin, but this time I'm going to pipe it.

Pass in a Grep and then enter the keyword zip. You'll find that in this case I get a much smaller subset back in the results. And if I need to refine it further, then I can also apply the different flags to look for an exact match, a partial match or ignore case sensitivity.
'''