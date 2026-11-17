


LESSON OVERVIEW
In the last lesson, you learned that a program is a set of instructions that tells a computer what to do. But instructions alone don't accomplish anything. A recipe with no ingredients doesn't produce a meal, and a program with nothing to work on doesn't produce a result.

That "something to work on" is data.

You've already seen the word. When we looked at the relationship between computers, programs, and data, we said a program tells a computer what to do with data. Now it's time to slow down and actually answer the question: what is data, exactly?

 




What Is Data?
Data is information represented in a form a computer can store, move, and process.

That's a fairly abstract definition, so let's ground it. Think about a simple online store. To sell a product, the store needs to keep track of things like:

A product's name
Its price
How many are in stock
A customer's name
Their email address
The quantity they want to buy
None of these are instructions. None of them say "do this, then do that." They're just facts — pieces of information about the world that the program needs in order to do its job.

That's the core idea: data is the raw material. The program is what acts on it.

Go back to the coffee example from the last lesson. The instructions were the program:

Get a cup.
Put coffee in the cup.
Boil water.
Pour the water in.
Stir.
But notice something. The instructions alone don't tell you how much coffee, how much water, or how hot. Those specifics — "two spoons of coffee," "300ml of water," "95 degrees" — are data. The program describes the process in general terms; the data fills in the specifics for one particular cup of coffee.

Same program. Different data. Different cup of coffee.

That's a pattern worth holding onto: a single program can usually be reused with many different pieces of data, producing a different result each time.

 


How It Works: Data Represents Something Real
Here's a detail that's easy to skim past but genuinely matters: data isn't the thing itself. It's a representation of the thing.

When a school system stores a student's grade, it isn't storing the student. It's storing a number, or a letter, that stands in for a fact about the student. When a banking app shows your balance, it isn't showing you a pile of physical cash — it's showing a number that represents how much money the bank's records say you have.

This matters because it explains a lot of what programming is actually about: deciding how to represent real-world things as data the computer can work with.

Consider a customer in an online store. In real life, a customer is a whole person — they have a name, a history, preferences, moods, a physical address. The program doesn't need all of that, and it can't capture all of that. It needs the parts that are relevant to the task:

Name (so the order can be labeled)
Email (so a receipt can be sent)
Shipping address (so the package can be delivered)
Everything else about that person — their sense of humor, what they had for breakfast — isn't part of the data, because the program has no use for it.

This is the first real design decision most programmers make, often without noticing they're making it: choosing which facts about the real world are worth turning into data, and which aren't.

 


Worked Example: A Shopping Cart
Let's make this concrete with the shopping cart example from the last lesson.

Suppose someone adds three items to their cart:

A notebook priced at 500
A pen priced at 100, with 2 being purchased
A water bottle priced at 1,200
Just by listing this out, you've already produced data. Each item has a name, a price, and, for the pen, a quantity. None of these numbers or words are instructions — they don't tell the computer to do anything by themselves. They're just facts about what's in the cart right now.

The program is a separate thing: a set of instructions that says something like "for each item, multiply its price by its quantity, then add all of those amounts together." That set of instructions, applied to this specific data, produces a total.

Swap in a different cart — different items, different prices, different quantities — and the same program produces a different total. The program didn't change. The data did.

This is why programmers often say "the data drives the behavior." The instructions stay fixed; the data determines what actually happens when those instructions run.

 


The "Wait, Why?" Moment
You might be wondering: if data is just information, why does it need to be a separate concept from the program at all? Why not just build the numbers directly into the instructions?

You actually could, for something as small as a single cup of coffee or a single cart. But think about what happens at scale. An online store doesn't process one order — it processes thousands, each with different products, different customers, different quantities. If the prices and names were baked directly into the instructions, you'd need a completely new program for every single order.

Separating data from the program is what makes a program reusable. The instructions describe a general process — "calculate the total of these items" — and the data supplies the specifics for one particular case. Write the process once; feed it different data as many times as you need.

This is also why, when something goes wrong in a program, experienced programmers often ask two separate questions rather than one: "Is the logic wrong, or is the data wrong?" A program can be written perfectly and still produce a wrong result if it's given bad data — a mistyped price, a missing quantity, an empty cart it wasn't prepared for. Keeping the two ideas distinct in your head is what lets you diagnose which one is actually the problem.

 


Common MISTAKES
A common assumption early on is that "data" only means numbers — prices, quantities, scores. It doesn't.

A customer's name is data. An email address is data. A yes-or-no answer to "is this item in stock?" is data. A photo, a paragraph of text, an audio clip — all data. Anything that represents information the program needs to store or act on counts.

It's also worth noting: not all data looks the same, and different pieces of information behave differently. A price behaves like a number — you can add it, multiply it. A name doesn't — it doesn't make sense to "add" two customer names together. You don't need to memorize categories of data yet; for now, just notice that data comes in different kinds, and a program has to treat each kind appropriately for what it represents. You'll work with this directly soon.

 


Application
You've already been surrounded by data represented on a computer, even before touching a program yourself:

A contact saved in a phone — name, number, maybe a photo.
A song in a playlist — title, artist, duration.
A message in a chat app — the text itself, the sender, the time it was sent.
In every one of these, some real-world thing — a person, a song, a conversation — has been turned into information a computer can store and display. That's data, doing exactly what it does in the systems you'll eventually build: standing in for something real, so a program has something concrete to work with.

 


Summary
You now have the second half of the picture that started in the last lesson. A program is the set of instructions. Data is the information those instructions act on — a representation of something real, shaped into a form the computer can store and process.

Held together, the relationship is simple:

Data → Program Instructions → Computer Performs the Work → Result
Different data through the same program produces different results. That single idea is behind almost everything you'll build from here: a program written once, reused endlessly, because the data keeps changing.

 


Additional Resources
Resource	Description	URL
What Is Data in Computing? 	A plain-language look at what data is and how computers use it, with no programming knowledge assumed.	https://youtu.be/PEWMgtu-1e4?si=WWk65IavbgO1YfvN
Data (computer science) — Wikipedia	A broader reference on how data is represented and handled, useful background before you meet any specific language.	https://en.wikipedia.org/wiki/Data_(computer_science)
Lessons in this topic
01
PY - LESSON 1.8: WHAT IS DATA?
In this lesson

LESSON OVERVIEW

What Is Data?

How It Works: Data Represents Something Real

Worked Example: A Shopping Cart

The "Wait, Why?" Moment

Common MISTAKES

Application

Summary
