# git_practical_exercices_interactive_rebase
This repository is the base for a practical git exercise.
This exercise is an intermediate level one and it is focusing on practising interactive rebase.

## Exercise:

The final goal of the exercise is to have the following commits in the following order in this repository:

1. Commit message: "Initial commit", this commit contains the readme file and the tester script, keep this commit unchanged!
2. Commit message: "First commit", Content: Add "First line" as the first line of the file "content".
3. Commit message: "Second commit", Content: Add "Second line" as the second line of the file "content".
4. Commit message: "Third commit", Content: Add "Third line" as the third line of the file "content".
5. Commit message: "Fourth commit", Content: Add "Fourth line" as the fourth line of the file "content".
6. Commit message: "Fifth commit", Content: Add "Fifth line" as the fifth line of the file "content".
7. Commit message: "Sixth commit", Content: Add "Sixth line" as the sixth line of the file "content".
8. Commit message: "Seventh commit", Content: Add "Seventh line" as the seventh line of the file "content".

## Hints:

If you take a look on the current log, you can see that there are several issues to be fixed in order to reach the above mentioned state of the repository.
The following actions are to be done:

1. Edit the content of the commit "Second commit" and fix it's content (change "Second ln" to "Second line").
2. Change the order of the commit, "Third commit - part 1" should be followed by "Third commit - part 2", which should be followed by "Fourth commit".
3. The commits "Third commit - part 1" and "Third commit - part 2" shall be squashed into one commit, its message should be "Third commit".
4. The commit message "Fourth" should be changed to "Fourth commit".
5. The commit "To be deleted" should be deleted.
6. The commit "Fifth and sixth lines" should be splitted into two commits: "Fifth commit", containing the addition of the "Fifth line" and "Sixth commit", containing the addition of the "Sixth line".

The action can be done in almost any order. They can be done by the application of interactive rebase once or multiple times.
You can verify your solution by running the file check.py in the repository.
