'''
Programming is no different and sometimes you need to revisit old code.

In this video, I'll guide you through how to use git diff to compare changes across your files branches and commits

The git diff command it goes a step further and tells you what exactly these changes are. 

When used together, you can think of them as a file system. Git status tells you the file names, but to open the file and see the contents, you'll need to use git diff.

Let's go into a more detailed example. In this video, I'll show you how you can use git diff.

Diff is used to make comparisons against files on your local repository. It can also be used against commits and against branches. I'll start with a simple example.

When I go into my local repository, I'll find a file called READ ME that I'd like to update slightly. You can do this with any editor such as VS code. I can also do this by executing the Vim command to enter the file for editing, remove a few words, and then save it. If you would like to learn more about Vim, there is a link to an additional reading at the end of this lesson.

Next, I'm going to use the git diff tool to compare the updated file against the head. Because we haven't yet completed a commit. It's not available for a comparison against another commit. 

I'll input git diff passing the head as the first option, and then finally the file name. This then returns an output showing the changes that occurred in each file. Here, the line starting with a minus symbol represents what it originally was. While the line with a plus symbol shows what it is now.

My example tells me that the words minor update have been removed. In addition to individual files, you can also make comparisons against previous commits.

 I'll start by using the git log command to display my history of commits. I'll also use the pretty flag here so that each one is shown in one line. The pretty flag is used by developers to make the output more readable. Each commit has its own ID code.

 So I'll perform a git diff command on the codes from the most recent commit and from the very first one.

 Git hub will go through all the files, note all the changes that have occurred, and return the differentiation between the two. Finally, one more way of using git diff that I'll show you is how to use it for making comparisons against branches.

If I perform the command git branch, it will display all the branches that are available in the repository. I can then use the git diff command to pass in my main branch, followed by my feature branch as the second option. Once again, this will display all the changes that have occurred between the two.

This shows that my feature branch has the previous update, while the main branch has the most recent one. 
'''