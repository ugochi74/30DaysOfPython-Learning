
Talent Nation

Overview
Dashboard

Learning
Learn
Arena

Progress
Missions
Inspections
Gates
Leaderboard
Achievements

Community
Academy Square

Account
Notifications
Profile
Sign out
Sat, Sep 5, 3:26 AM GMT+1
1d streak


CO
Back to Dashboard
Back to topic
Lesson 3: Environment Architecture & command
Lesson 3.1.4 CORE CLI COMMANDS
Lesson 4 of 5
5 min read
1 video
You can move on now.

The next button is unlocked. The linked drill is now available too.





Lesson content
The command grammar
Before we look at individual commands, let us understand the grammar of a command line.

A typical command has this structure:

command [options] [arguments]
The command is the name of the program you want to run. The options modify how the command behaves. Options often begin with a dash - or two dashes --. The arguments are the targets or inputs for the command.

For example:

ls -la /home/amaka
Here:

ls is the command.
-la are options: -l means long format, -a means all files, including hidden ones.
/home/amaka is the argument: the directory to list.
Not all commands require options or arguments. For example:

pwd
has no options or arguments. It simply prints the current directory.

Understanding this grammar helps you read unfamiliar commands. The command is the action. Options are how the action is performed. Arguments are what the action is performed on.

 

pwd — print working directory
You have already seen pwd. It prints your current location.

pwd
Output:

/home/amaka/ai_projects
Use pwd often. It is the best way to confirm where you are.

 

ls — list directory contents
ls lists the files and directories inside a directory.

Basic usage:

ls
This lists the contents of the current directory in a simple format.

If you want to list the contents of another directory, pass its path as an argument:

ls /home/amaka/documents
ls has many useful options.

ls -l gives a long listing with permissions, size, and date.
ls -a shows hidden files, which begin with a dot.
ls -la combines both.
For example:

ls -la
Output might look like:

drwxr-xr-x  2 amaka amaka 4096 Jun  1 12:00 .
drwxr-xr-x  5 amaka amaka 4096 Jun  1 11:50 ..
-rw-r--r--  1 amaka amaka   42 Jun  1 12:00 core.py
Here you can see . and .. as actual entries. You can also see core.py with its size and modification date.

ls is one of the commands you will use most frequently. It tells you what is around you.

 

cd — change directory
cd changes the current working directory.

Basic usage:

cd /home/amaka/documents
This moves you to the specified directory.

To go to a subdirectory, use a relative path:

cd documents
To go up one level:

cd ..
To go home:

cd ~
Or simply:

cd
When cd is used without an argument, it returns to the home directory.

cd is how you move through the file system.

 

mkdir — make directory
mkdir creates a new directory.

Basic usage:

mkdir ai_projects
This creates a directory called ai_projects inside the current directory.

To create multiple directories at once, list them:

mkdir data scripts notebooks
This creates three directories.

To create a nested directory structure in one command, use the -p option:

mkdir -p ai_projects/data/raw
The -p option tells mkdir to create parent directories as needed. If ai_projects or data does not exist, mkdir -p creates them too.

This is especially useful when scaffolding projects.

 

touch — create an empty file or update a timestamp
touch is commonly used to create an empty file.

Basic usage:

touch core.py
If core.py does not exist, touch creates a new empty file with that name. If it already exists, touch updates its modification timestamp without changing its contents.

touch is simple but very useful when you need to create files from the terminal.

 

A practical command sequence
Let us walk through a realistic terminal session. Imagine a developer named Amaka wants to start a new Python project.

She opens a terminal and runs:

pwd
Output:

/home/amaka
She creates a project directory:

mkdir ai_projects
She moves into it:

cd ai_projects
She checks where she is:

pwd
Output:

/home/amaka/ai_projects
She creates a Python file:

touch core.py
She lists the contents:

ls -la
Output:

total 8
drwxr-xr-x  2 amaka amaka 4096 Jun  1 12:00 .
drwxr-xr-x  5 amaka amaka 4096 Jun  1 11:50 ..
-rw-r--r--  1 amaka amaka    0 Jun  1 12:00 core.py
Notice that core.py has size 0. That is because touch creates an empty file.

Now she has a clean project directory. In the next sub-lesson, she will add Python code to the file and run it.

 

Command chaining and semicolons
Sometimes you want to run multiple commands in one line. You can separate commands with a semicolon:

mkdir ai_projects; cd ai_projects; touch core.py
This runs all three commands one after another, no matter what. For simple sequences, this is convenient. But there are also more advanced operators such as &&, which stops if a command fails. For now, the semicolon is enough to understand.

 
Common mistakes and misconceptions
A common mistake is to type ls -la and expect it to list a specific directory without providing the path. ls -la lists the current directory. To list another directory, add it as an argument.

Another mistake is to use cd with a file instead of a directory. This produces an error like Not a directory.

A third mistake is to create a file with touch and then expect it to have contents. It will be empty. You must edit it later with a text editor or command.

A fourth mistake is to forget the -p option when using mkdir to create nested directories. Without -p, mkdir ai_projects/data fails if ai_projects does not exist.

A fifth mistake is to confuse options and arguments. Options usually start with a dash. Arguments are the targets.

 
Summary
Commands have a grammar: command, options, arguments.
pwd prints the current directory.
ls lists directory contents.
cd changes directories.
mkdir creates directories.
touch creates empty files or updates timestamps.
Options modify behavior, such as -l and -a for ls.
You can chain commands with semicolons.
 
Additional Resources
GNU Coreutils Manual
LinuxCommand.org: Shell Basics
Ubuntu Community Help: UsingTheTerminal
Microsoft Learn: Windows Terminal basics
Lessons in this topic
01
Lesson 3.1.1 THE SHELL ENVIRONMENT: COMMUNICATING DIRECTLY WITH THE KERNEL VIA BASH
02
Lesson 3.1.2 FILE SYSTEM NAVIGATION
03
lesson 3.1.3 PYTHON RUNTIMES AND THE $PATH VARIABLE
04
Lesson 3.1.4 CORE CLI COMMANDS
05
Lesson 3.1.5 HEADLESS EXECUTION: RUNNING SCRIPTS WITHOUT A GRAPHICAL USER INTERFACE (GUI)
In this lesson

Lesson content

The command grammar

pwd — print working directory

ls — list directory contents

cd — change directory

mkdir — make directory

touch — create an empty file or update a timestamp

A practical command sequence
Next