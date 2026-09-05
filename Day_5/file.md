
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
Sat, Sep 5, 3:18 AM GMT+1
1d streak


CO
Back to Dashboard
Back to topic
Lesson 3: Environment Architecture & command
Lesson 3.1.2 FILE SYSTEM NAVIGATION
Lesson 2 of 5
7 min read
1 video
You can move on now.

The next button is unlocked. The linked drill is now available too.





LESSON CONTENT
The file system is a tree
Every file on your computer lives inside a directory. A directory is the same thing as a folder. Directories can contain files and other directories. This creates a branching structure that looks like an upside-down tree.

At the very top of the tree is the root. On Linux and macOS, the root is represented by a single forward slash /. On Windows, each drive has its own root, such as C:\.

Think of the file system like a large estate in Lagos. The root is the main gate. From the main gate, there are roads leading to different streets. Each street has houses. Each house has rooms. A file is like a document or item inside a room.

A directory is like a room that can contain items and other rooms. A file is like a specific item, such as a book or a box. This mental model will help you understand paths.

 

Absolute paths
An absolute path gives the full address of a file or directory from the root. It does not depend on where you are currently located.

On Linux or macOS, an absolute path always starts with /. For example:

/home/amaka/documents/report.txt
This means:

Start at the root /.
Go into the home directory.
Go into the amaka directory.
Go into the documents directory.
The file is report.txt.
On Windows, an absolute path might look like:

C:\Users\Amaka\Documents\report.txt
Here, C:\ is the root of the C drive, and the path follows the same structure but uses backslashes.

An absolute path is like giving a full address: “No. 15, Adeola Odeku Street, Victoria Island, Lagos.” Anyone can follow it from any starting point because it includes the full route.

 

Relative paths
A relative path gives the location of a file or directory relative to your current directory. It does not start from the root.

For example, if you are already inside /home/amaka, the relative path to the report file is:

documents/report.txt
This means: from where I am, go into the documents directory, then get report.txt.

A relative path is like telling someone, “Go to the next street and enter the third house on your right.” That instruction only makes sense if the person knows where they are standing. If they are standing somewhere else, the same instruction leads to a different place.

This is why programmers must always know the current working directory.

 

Current working directory
The current working directory, often shortened to cwd or working directory, is the directory the shell is currently inside.

Every process, including your shell, has a current working directory. Relative paths are resolved against this directory. If you run:

cd documents
and your current working directory is /home/amaka, you will move to /home/amaka/documents. If your current directory was /tmp, the same command would attempt to move to /tmp/documents.

This is very similar to standing in a market and being told, “Go to the yam sellers.” The direction only makes sense if you know which part of the market you are standing in.

 

The pwd command
To see your current working directory, use:

pwd
pwd stands for print working directory. It prints the absolute path of the directory you are currently in.

For example:

pwd
Output:

/home/amaka
This tells you exactly where you are. It is one of the most important commands for avoiding confusion.

 

The special symbol .
In every directory, there is a hidden reference to the current directory itself. That reference is . (a single dot).

If you run:

cd .
you will stay in the same directory. Why is this useful? It appears in path constructions and when you want to run a script in the current directory. For example, you might see:

./script.py
The ./ means “in this current directory.” It tells the shell to look for script.py right here, not in the search path.

Think of . as the word “here.” When someone says, “Put the box here,” they mean the current location.

 

The special symbol ..
Every directory also has a reference to its parent directory, represented by .. (two dots).

If you are inside /home/amaka/documents, then .. refers to /home/amaka. If you run:

cd ..
you move one level up.

.. is like saying, “Go back to the street from this compound.” It takes you outward, toward the root.

You can chain .. to go up multiple levels. For example:

cd ../..
from /home/amaka/documents would first go to /home/amaka, then to /home.

 

The home directory and ~
Every user account has a home directory. On Linux or macOS, a user named amaka might have the home directory /home/amaka. On Windows, it might be C:\Users\Amaka.

The home directory is your personal space. When you open a terminal, it usually starts in your home directory.

The shell gives you a shortcut for this: ~ (the tilde character). Wherever you see ~, it refers to the current user’s home directory.

For example:

cd ~
moves you to your home directory.

cd ~/documents
moves you to the documents folder inside your home directory.

The ~ symbol is a convenience. It saves you from typing the full path every time.

 

Absolute vs. relative: why it matters
Understanding the difference between absolute and relative paths prevents many errors.

Imagine you are in /home/amaka/projects. You want to open a file located at /home/amaka/documents/report.txt.

Using a relative path, you would write:

cat ../documents/report.txt
Because .. moves up from projects to amaka, then documents/report.txt continues from there.

Using an absolute path, you would write:

cat /home/amaka/documents/report.txt
Both commands work. But if you later run the same relative path from a different directory, it may fail. This is why knowing your current directory is essential.

A good habit is to run pwd before using relative paths. It shows you the context.

 

A file system analogy
Think of the file system like the national postal system.

An absolute address might be:

Plot 12, Aguiyi Ironsi Street, Maitama, Abuja
This is an absolute location. A letter with this address can be delivered regardless of where the postal worker starts.

A relative direction might be:

From the post office, turn left at the next junction. The house is the fourth on the right.
This only works if the postal worker starts from that specific post office. If the worker starts from a different post office, the directions fail.

When you use a relative path, you are giving directions from the current working directory. When you use an absolute path, you are giving a full address from the root.

 

Traversing the tree
Let us practice a small navigation sequence. Suppose you are at:

/home/amaka
You want to go to:

/home/amaka/ai_projects/data
You can move step by step:

cd ai_projects
cd data
Now your current directory is /home/amaka/ai_projects/data.

Or you can do it in one command:

cd ai_projects/data
Both work. The second is faster.

If you want to go back home from anywhere, use:

cd ~
If you want to go back one level, use:

cd ..
These simple commands are the foundation of shell navigation.

 

Common mistakes and misconceptions
A common mistake is to use \ instead of / on Linux or macOS. Linux and macOS use forward slashes. Windows traditionally uses backslashes, but modern tools often accept forward slashes in some contexts. When you are in a Bash shell on Linux or macOS, always use /.

Another mistake is to type cd documents from the wrong directory. If the directory does not exist in your current location, the shell will say something like No such file or directory.

A third mistake is to assume ~ means the same as root. It does not. ~ is the user’s home, while / is the root of the entire file system.

A fourth mistake is to forget that relative paths depend on the current working directory. A path like documents/report.txt is not the same everywhere.

A fifth mistake is to ignore the difference between . and ... One means “here,” the other means “one level up.”

 

Summary
The file system is a tree with a root at the top.
Absolute paths start from the root.
Relative paths start from the current working directory.
pwd prints the current working directory.
. means the current directory.
.. means the parent directory.
~ means the home directory.
Knowing your working directory prevents path errors.
 
Additional Resources for 3.1.2
GNU Coreutils: pwd invocation
LinuxCommand.org: Files and Directories
Ubuntu Community Help: LinuxFileSystemTree
MDN Web Docs: File system paths (conceptual)
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

LESSON CONTENT

The file system is a tree

Absolute paths

Relative paths

Current working directory

The pwd command

The special symbol .

The special symbol ..
Next