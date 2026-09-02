

Talent Nation
Dashboard
Learn
Arena
Missions
Inspections
Gates
Leaderboard
Achievements
Academy Square
Notifications
Profile
Sign out
Wed, Sep 2, 10:37 AM GMT+1
1d streak
CO
Back to Dashboard
Back to topic
Lesson 1: What Is Programming
LESSON 1.1.3 STATE TRANSFORMATION: TRACKING DATA THROUGH AN EXECUTION PIPELINE
Lesson 3 of 4
8 min read
1 video

You can move on now.

The next button is unlocked. The linked drill is now available too.


Data changes as instructions run

Think about what happens when you send ₦3,000 from your bank account to a friend's account.

Before the transfer, your balance might be ₦10,000. Your friend's balance might be ₦2,000. After the transfer, your balance should be ₦7,000, and your friend's balance should be ₦5,000. The money did not move as physical cash, but the recorded information changed.

In programming, we call the recorded information state. State is the data that describes a situation at a particular moment. As a program runs, state changes step by step. A programmer must track those changes carefully.

This is the idea behind state transformation. An execution pipeline is a series of steps that takes an initial state, transforms it through one or more operations, and produces a final state.


Input → Process → Output

A simple way to understand state transformation is the pattern:

Input → Process → Output

Every meaningful program has these three stages.

    Input is the data that enters the system.
    Process is the set of operations that transforms the input.
    Output is the resulting data after processing.

For example, at an ATM:

    Input: your card, PIN, and requested amount.
    Process: verify PIN, check balance, subtract amount.
    Output: cash dispensed and a receipt.

The state before processing is the initial state. It includes the balance, the requested amount, and whether the PIN is correct. The state after processing is the final state. It includes the updated balance, the cash dispensed, and the receipt.

This pattern appears everywhere. A calculator takes numbers as input, processes them with arithmetic, and outputs a result. A search engine takes a query, processes it through ranking logic, and outputs results. A WhatsApp message takes text, processes it through the network, and outputs the message on the other person's phone.


What is state?

State is not a special programming language feature. It is simply the current values of the data a program is working with.

For example, in a banking app, the state might include:

    The user's account number.
    The user's current balance.
    The recipient's account number.
    The recipient's current balance.
    The amount being transferred.
    The transaction receipt.

Each of these pieces of information can change as the program runs. Some pieces change, and some stay the same. The combination of all these values at a given moment is the state.

A simple way to think about state is to think of labeled boxes. Each box has a name, and each box holds a value. In programming, these labeled boxes are often called variables.

For example:

balance = 10000 amount = 3000 receipt = empty

Here, balance is a box that holds the value 10000. amount holds 3000. receipt is empty. This is the initial state.


State changes step by step

Let us trace a simple transfer as an execution pipeline. We will use plain English and a table to see how the state changes.

Initial state:
Label 	Value
balance 	10000
amount 	3000
recipient_balance 	2000
receipt 	empty


Step 1: Check that amount is less than or equal to balance.

The check succeeds because 3000 <= 10000. We might record this as:
Label 	Value
check_passed 	true


Now the state includes a new piece of information: check_passed is true.

Step 2: Subtract amount from balance.

The new balance is 10000 - 3000 = 7000. The state changes:
Label 	Value
balance 	7000
amount 	3000
recipient_balance 	2000
receipt 	empty


Step 3: Add amount to recipient_balance.

The recipient's new balance is 2000 + 3000 = 5000.
Label 	Value
balance 	7000
amount 	3000
recipient_balance 	5000
receipt 	empty


Step 4: Create a receipt.

The receipt might be a message: "₦3,000 sent to friend."
Label 	Value
balance 	7000
amount 	3000
recipient_balance 	5000
receipt 	"₦3,000 sent to friend"


This is the final state.

Notice how we tracked each box and how its value changed. If we skipped Step 2, the balance would remain ₦10,000, and the transfer would not be reflected in the records. If we skipped Step 3, the recipient would not receive the money. If we forgot to update the receipt, the user would not see confirmation.


Execution pipeline

An execution pipeline is simply a sequence of state transformations. Each step reads some part of the current state, does something with it, and produces a new state for the next step.

The word pipeline is useful because it suggests data flowing through stages. At each stage, the data is changed in a specific way, just as crude oil is refined through different stages or rice is processed through milling, bagging, transporting, and selling.

For example, a simple user login pipeline might look like this:

    Take the user's email and password.
    Find the stored password for that email.
    Compare the entered password with the stored password.
    If they match, set login_status to success.
    If they do not match, set login_status to failure.
    Send the login_status back to the user interface.

Each step transforms the state. The email and password are part of the state. The stored password is part of the state. The login_status is new state created during the process.


Why tracking state matters

In programming, many bugs happen because a programmer loses track of state.

Imagine a step says "subtract the amount," but the programmer forgot that the balance had already been reduced in an earlier step. The balance might be reduced twice. That would be a serious banking error.

Imagine a step says "show the receipt," but the receipt has not been created yet. The user sees an empty message.

Imagine a step says "check if the email exists," but the email was not stored properly in a previous step. The check fails even though the email is valid.

Tracking state means knowing exactly what each box contains before and after every step. It is like keeping a mental ledger of the program's data.


A cooking analogy

Cooking is also a series of state transformations.

Consider making tomato stew.

Initial state:

    Tomatoes: raw, whole
    Onions: raw, whole
    Oil: cold
    Pot: empty

Step 1: Blend the tomatoes and onions.

Now the tomatoes and onions are a liquid mixture.

Step 2: Pour oil into the pot and heat it.

Oil state changes from cold to hot.

Step 3: Pour the blended mixture into the hot oil.

The mixture changes from raw liquid to frying stew.

Step 4: Add salt and seasonings.

The taste state changes.

Step 5: Cook for ten minutes.

The stew thickens and the flavor develops.

At each stage, the ingredients are transformed. If you skip Step 1 and put whole tomatoes in hot oil, the result is different. If you skip Step 2 and pour the mixture into cold oil, the result is also different. The final state depends on each intermediate state.

This is exactly how software works. Data flows through steps, and each step transforms it.


State and variables

In programming, we store state in variables. A variable is simply a named container for a value. The value can change over time, but the name stays the same.

For example:

balance = 10000 balance = 7000

The first line sets the box balance to 10000. The second line changes the box balance to 7000. The old value is gone. The label remains.

This is how state transformation happens in a program. We assign new values to variables as steps run. The order matters because later values overwrite earlier ones.

If you are new to programming, the idea of a variable may seem odd. But you already use variables in everyday life. Your bank balance is a variable. The number of calls you have made on your phone is a variable. The price of fuel is a variable. It is a label with a value that can change.


Common mistakes and misconceptions

One common mistake is to think that state updates automatically. It does not. If you subtract money from one account, the recipient's account does not automatically increase unless you write a step to do so. Computers do not infer effects; they only do what the steps say.

Another mistake is to use a stale value. Suppose you store the balance in a variable, then later subtract money, but you forget to update the variable. Any later step that reads the variable will see the old balance.

A third mistake is to confuse the label with the value. balance is not ₦10,000. balance is the box that currently holds ₦10,000. This distinction becomes important later.

A fourth mistake is to lose track of intermediate state. A process may have many small changes. If you do not write them down or trace them, it is easy to miss one.


Summary

    State is the current data a program is working with.
    Variables are named containers that hold state.
    Every program can be understood as input, process, and output.
    An execution pipeline is a sequence of state transformations.
    Each step reads some state and produces new state for the next step.
    Tracking state carefully prevents bugs and logical errors.
    Cooking, banking, and many real-world processes are forms of state transformation.



Additional Resources

    Khan Academy: Intro to Variables
    MDN Web Docs: Storing the information you need — Variables
    BBC Bitesize: Variables and constants
    Crash Course Computer Science: Instructions and Programs

Lessons in this topic
01
LESSON 1.1.1 THE DETERMINISTIC NATURE OF COMPUTE: NO MAGIC, JUST INSTRUCTIONS
02
LESSON 1.1.2 ALGORITHMIC SEQUENCING: DECONSTRUCTING COMPLEX GOALS INTO ATOMIC OPERATIONS
03
LESSON 1.1.3 STATE TRANSFORMATION: TRACKING DATA THROUGH AN EXECUTION PIPELINE
04
LESSON 1.1.4 THE SYNTAX-AGNOSTIC MINDSET: ENGINEERING LOGIC BEFORE LANGUAGE
In this lesson
