
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
Sat, Sep 5, 3:22 AM GMT+1
1d streak


CO
Back to Dashboard
Back to topic
Lesson 3: Environment Architecture & command
lesson 3.1.3 PYTHON RUNTIMES AND THE $PATH VARIABLE
Lesson 3 of 5
6 min read
1 video
You can move on now.

The next button is unlocked. The linked drill is now available too.



What is a runtime?
A runtime is the environment that executes a program. When you run Python code, the Python runtime is the interpreter plus the supporting files and libraries that make execution possible.

You can think of a runtime like a generator. If you buy an electric appliance, it needs electricity from a generator or the national grid. The appliance alone cannot work. The runtime is the electricity and the generator. Python source code is the appliance. The Python runtime is what powers it.

In the previous lesson, you learned that CPython is the standard Python implementation. CPython is the runtime that compiles Python source to bytecode and executes it on the Python Virtual Machine. When someone says “Python is installed on my system,” they usually mean the Python runtime is available.

 

Where is Python located?
Python is just a program stored somewhere in the file system. On Linux, it might be at:

/usr/bin/python3
On macOS, it might be at:

/opt/homebrew/bin/python3
On Windows, it might be at:

C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe
The exact location depends on how Python was installed. But you rarely need to type the full path. When you type:

python
or:

python3
the shell finds the Python executable for you. How does it know where to look? The answer is the $PATH variable.

 

What is an environment variable?
An environment variable is a named value stored by the operating system that programs can read. It is like a global setting.

For example, an environment variable called HOME might store the path to your home directory. An environment variable called LANG might store your language preference.

Environment variables are used by the shell and by many programs to configure behavior. The $PATH variable is one of the most important.

 

The $PATH variable
The $PATH variable is a list of directories. When you type a command, the shell searches these directories for an executable file with that name.

If you type:

python
the shell looks in the first directory listed in $PATH. If it does not find a file named python there, it looks in the next directory, and so on. The first matching executable is the one it runs.

The directories in $PATH are separated by colons on Linux and macOS. A typical $PATH might look like this:

/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
On Windows, the separator is a semicolon. But the concept is the same.

You can see your $PATH by running:

echo $PATH
The $ before PATH tells the shell to substitute the value of the variable. The output is your current search path.

 

A Lagos street search analogy
Imagine you are a delivery rider in Lagos. You receive an order for a customer named “Python.” You do not know the customer’s exact address. But you have a list of areas to search. You start with the first area on the list, then the next, then the next. When you find the customer with that name, you deliver the order.

That list of areas is like $PATH. The customer’s name is the command. The shell searches each directory in order until it finds the executable.

If the customer is not in any area on your list, you cannot deliver the order. That is why you get an error like python: command not found when Python is not in $PATH.

 

How $PATH lookup works in detail
Let us say your $PATH is:

/usr/local/bin:/usr/bin:/bin
And you type:

python3
The shell checks these in order:

/usr/local/bin/python3 — Does it exist and is executable?
/usr/bin/python3 — Does it exist and is executable?
/bin/python3 — Does it exist and is executable?
If it finds an executable at step 2, it stops searching and runs that file. If it reaches the end without finding anything, it prints:

python3: command not found
This lookup happens for every command you type, whether it is ls, pwd, mkdir, or python.

 

which python and where python
To find out which Python executable the shell will run, use which on Linux or macOS:

which python
Output might be:

/usr/bin/python
Or:

which python3
Output:

/usr/bin/python3
On Windows, the equivalent command in the command prompt is where:

where python
Output might be:

C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe
These commands are diagnostic. They show you exactly which file the shell resolves for a command name. This is very useful when you have multiple Python installations and want to know which one is active.


Multiple Python versions
Many systems have more than one Python version installed. For example, a Linux system may have both Python 2 and Python 3. Because Python 2 is now deprecated, modern systems often use python3 for Python 3. On some systems, python may still point to Python 2, or it may not exist at all.

This is why you may see commands like:

python3 --version
Instead of:

python --version
On Windows, the py launcher is often used. You may see:

py --version
Do not worry if your system behaves slightly differently. The key idea is that the shell uses $PATH to find the right executable.

 
Checking the Python version
To verify that Python is installed and see the version, run:

python --version
or:

python3 --version
Output might be:

Python 3.12.1
The version number tells you which major and minor release you have. For example, Python 3.12.1 means major version 3, minor version 12, patch version 1.

If you get command not found, Python may not be installed, or the executable may not be in your $PATH. In that case, you need to install Python or adjust your $PATH.


The order of directories in $PATH matters
The shell uses the first match. If you have two Python executables, one in /usr/local/bin and another in /usr/bin, the one in the earlier directory in $PATH wins.

This can cause confusion. You may think you are using Python 3.12, but the shell resolves to Python 3.9 because of path order.

This is why which python is so helpful. It tells you the truth.

 
Changing $PATH
You can change $PATH in a terminal session by assigning a new value. For example:

export PATH="/opt/my_python/bin:$PATH"
This prepends /opt/my_python/bin to the existing $PATH. The export command makes the variable available to child processes. After this, any command you run will search /opt/my_python/bin first.

This is an important concept, but for now you may not need to modify $PATH. The important thing is to understand how lookup works.



Common mistakes and misconceptions
A common mistake is to assume that python and python3 are always the same. On many systems, they are not. Always check with which and --version.

Another mistake is to install Python but then find the shell says python: command not found. This usually means the installation directory was not added to $PATH. Reinstalling with the option to add to PATH, or manually updating $PATH, fixes it.

A third mistake is to trust the first Python you see in a file explorer. The shell may not use that one because $PATH points somewhere else. Use which to verify.

A fourth mistake is to edit $PATH blindly. Removing important directories can break your shell. If you make changes, do so carefully and understand why.

A fifth mistake is to think that $PATH is a Python concept. It is a general shell concept. It applies to all commands, not just Python.

 
Summary
The Python runtime is the interpreter plus supporting files.
Python is stored as an executable in a file system directory.
$PATH is a list of directories the shell searches for commands.
The first matching executable wins.
which shows the resolved path on Linux/macOS; where on Windows.
python --version confirms which Python is active.
Multiple Python versions can exist, and path order determines which runs.
 

Additional Resources
Python Documentation: Command line and environment
LinuxCommand.org: Environment variables
GNU Bash Manual: Environment
Microsoft Learn: About the PATH variable
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

What is a runtime?

Where is Python located?

What is an environment variable?

The $PATH variable

A Lagos street search analogy

How $PATH lookup works in detail

which python and where python

Multiple Python versions
Next