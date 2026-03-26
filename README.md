 Notes Management CLI Application
This is a Command Line Interface (CLI) application built with Python and SQLite. it is designed to help users 
           Add notes
           View notes
           Search notes and 
           Delete notes
 from their terminal.

 step 1: setting up working space
   dowmnload python https://www.python.org/downloads/⁠ using this link based on your windows and install it.
   install vscode which is a text editor to write the code.
   open vscode 
   create a folder named notes-cli 
   select the folder and create file main.py in the folder.

 step 2: writing code
    write the code 
    save the code to main.py
    a white circle on the tab means it is not saved.

step 3:running app
  open new terminal in the top menu and run the code using python3 main.py
  if error appears correct the error.
  Type 1 to add a note then press Enter. Type your note and press Enter again.
  there will be a file named notes.db under the main.py file which is read only for the computer to need. do not open it.

step 4: setting up git
  Download git from git-scm.com. Just click next on everything during the install.
  restart vscode.
  Type these two lines in the terminal:
    git config --global user.name "Your Name"
    git config --global user.email "your@email.com"
  Git won't let you save any pages until it knows who the owner is.
  Every time you save your code (a commit), Git attaches your name and email to that.
  You only have to do this once on your computer.

step5: pushing and connecting git
  Go to github.com and sign up.
  Click the + button to create New Repository. Name it notes-cli
  Copy the commands GitHub gives you and paste them into your VS Code terminal.
    git init (Starts the tracker)
    git add . (Picks up your files)
    git commit -m "commit" (Saves the version)
    git push -u origin main (Uploads it)

now it shows a new dashboard with branches and the files you created in vscode main.py file and your "Commit History"
  
