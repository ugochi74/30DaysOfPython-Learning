
Lesson OVERVIEW
You've learned about computers and how they follow instructions. But where do those instructions come from? They come from programming.

This lesson establishes the essential mental model that every programmer uses. By the end, you'll understand what programming actually is—and what it isn't.

 




LESSON CONTENT

Core Concept: Programming as Translation
Programming is the process of creating instructions that tell a computer how to perform a task.

But that definition alone doesn't capture what's really happening. Let's be more precise.

Programming solves a problem by:

Understanding what the problem is
Figuring out a sequence of steps that will solve it
Expressing those steps in a language the computer can execute
This is a crucial distinction. Programming is not primarily about memorizing syntax or typing code. Those are mechanical skills. The real skill is learning to break problems down into instructions a computer can follow.

 


The Mental Model: Problem → Algorithm → Code
When you program, you move through three distinct layers:

Layer 1: The Problem

What needs to be accomplished? This is the real-world situation you're addressing.

Layer 2: The Algorithm

A sequence of steps that solves the problem. This is language-agnostic—you can write it in plain English, draw it as a flowchart, or describe it out loud.

Layer 3: The Code

The algorithm expressed in a programming language (like Python). This is what the computer actually executes.

Here's the key insight: the algorithm is the important part. The code is just the expression of it. A good programmer thinks first about the algorithm, then about the code.

 


A Concrete Example
Let's trace a complete example from problem to code.

The Problem
Calculate the total price of two products.

The Algorithm
Get the price of product 1
Get the price of product 2
Add the two prices together
Produce the total

The Code (Python)
price1 = 10
price2 = 15

total = price1 + price2

print(total)
When this code runs, the computer executes each instruction in sequence. It doesn't "understand" what a product is or why you're adding numbers—it simply performs the operations you've instructed it to perform.

 


Wait, Why?
Here's where beginners often get confused:

"Why can't I just tell the computer 'calculate the total price' and be done with it?"

Because computers are literal. They have no context, no intuition, and no understanding of what "total price" means. Every single step must be spelled out explicitly.

This is why algorithms matter. When you're writing an algorithm, you're forced to think through every step a computer would need. You can't hand-wave. You can't assume the computer will "figure it out."

That frustration you might feel—the "why do I have to be so specific?" feeling—is actually the core of programming. Learning to think in explicit steps is what makes you a programmer, not learning a language's syntax.

 


What Programming Is Not
Let's clear up a common misconception: Programming is not "typing code."

A programmer spends a significant amount of time:

Understanding what problem they're solving
Asking questions to clarify requirements
Thinking about what could go wrong
Designing a solution before writing a single line
Testing and debugging
Reading and understanding existing code
Typing is the easy part. The thinking is the work.

 


The Role of Python
We're learning Python because it makes expressing instructions relatively straightforward. The syntax (the rules of the language) is designed to be readable. You can focus more on the algorithm and less on wrestling with the language.

But remember: Python is the tool, not the skill. The skill is problem-solving and algorithmic thinking.

 


Summary
Programming is the process of creating instructions for a computer. It requires you to think through problems systematically, design solutions (algorithms), and then express those solutions in a programming language.

The syntax and language details matter, but they're secondary. The primary skill is learning to think like a programmer—breaking problems into explicit, logical steps.

You already started doing this in Lesson 1.1 when you tried to give an assistant instructions to make a cup of coffee. Now you have a name for that process: it's the algorithm. And writing it in a language the computer can execute? That's programming.

 


Additional Free Resources
Here are supplementary free materials to help you strengthen your algorithmic thinking and understanding of programming fundamentals:

Interactive & Visual Algorithmic Practice
Resource	Focus	URL
MIT Scratch	Visual programming to practice Layer 2 (Algorithms) without syntax errors.	https://scratch.mit.edu
BBC Bitesize: Introduction to Computational Thinking	Beginner guide to decomposition, abstraction, pattern recognition, and algorithms.	https://www.bbc.co.uk/bitesize/guides/zp92xnb/revision/1

Courses & Video Lectures
Resource	Focus	URL
Harvard CS50: Introduction to Computer Science (Lecture 0)	Explains computational thinking and algorithmic problem-solving before diving into code.	https://www.edx.org/learn/computer-science/harvard-university-cs50-s-introduction-to-computer-science
Khan Academy: Intro to Algorithms	Step-by-step visual lessons on how algorithms work.	https://www.khanacademy.org/computing/computer-science/algorithms

Free Online Textbooks
Resource	Focus	URL
Automate the Boring Stuff with Python (Chapter 0 & 1)	Practical introduction to the programmer mindset and writing your first execution steps.	https://automatetheboringstuff.com
Python for Everybody (Chapter 1)	Understanding how programs talk to computers and how to construct logic.	https://www.py4e.com/html3/01-intro
Lessons in this topic
01
PY - LESSON 1.3: WHAT IS PROGRAMMING?
In this lesson

Lesson OVERVIEW

LESSON CONTENTCore Concept: Programming as Translation

The Mental Model: Problem → Algorithm → Code

A Concrete Example

The Problem

The Algorithm

The Code (Python)

Wait, Why?
