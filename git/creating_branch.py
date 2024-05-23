'''
Example
Let's run through a typical flow of creating a new branch and adding some new content.

Step 1: Clone the repository.

Step 2: Create a new branch.

git checkout -b test/forking-example 

Step 4: Create a new file and commit it to the repository.

touch text.txt
git add . 
git commit -m 'chore: testing' 

Step 5 Push the branch to your remote repository.

git push -u origin test/forking-example 

Step 6: Go to Github and click the Compare & pull request button. If it's not available, click on the branch dropdown button and change it from main to the branch name of test/forking-example:
'''