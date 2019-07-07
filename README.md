# git-using-command-line

This repository focuses on building a python application for doing commit,diff and display operations of git 
provided following rules are taken into account-
- The text that is composed of one or more lines.
- Each line has a maximum character width of 10 characters (including newline).
- The total number of lines is 20.

The following operations are permitted:
1. Appending a new line at the end of the file.
2. Modifying any existing line.
3. Deleting any existing line

Only one of the above operations can be done at a given time i.e., the user
can either append a line -or- delete a line. After each operation, the file
is commited using the git. 
