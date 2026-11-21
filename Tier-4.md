## Tier 4: Conceptual Challenge, Data Translator

### Identify the data

Customer information: name Victor, age 30, account balance 150000.50, account active Yes.

| Information | Kind of information | Why it needs its own representation |
|-------------|---------------------|-------------------------------------|
| Victor | Text (string) | Made of characters. You do not do arithmetic on a name. |
| 30 | Whole number (integer) | A quantity with no decimal part that can be compared or calculated with. |
| 150000.50 | Decimal number (float) | A quantity with a fractional part (money) that needs correct calculation. |
| Yes | True/false state (boolean) | One of two states that controls decisions, such as whether the account can be used. |

The computer must distinguish these because the type tells it which operations are valid. `30 + 5` makes sense, but `Victor + 30` does not.

### Go one level deeper: how is this information represented digitally?

```
Real-world information
        |
Data representation (text, integer, decimal, boolean)
        |
Numerical/digital representation
        |
Binary data (0s and 1s)
        |
Stored by the computer
```

| Information | Digital representation |
|-------------|------------------------|
| Victor | Each character has a numeric code (for example, in ASCII or Unicode), and each code is stored in binary. |
| 30 | Stored as a binary number. |
| 150000.50 | Stored in a number format that can hold decimals, also as binary. |
| Yes | Stored as one of two states, such as 1 for active and 0 for inactive. |

The same pattern of bits can mean different things depending on how it is interpreted. The data type gives the bits their meaning.

### Reasoning challenge: the balance is stored incorrectly

| Question | Answer |
|----------|--------|
| What could happen to the customer's account? | The balance would be wrong. For example, 150000.50 might appear as 15000050 or 1500.05. The customer could be refused money they really have, or be allowed to withdraw money they do not have. Fees, transactions, and reports built on that value would also be wrong. |
| Why does this matter? | The computer can only process information correctly when the stored representation is interpreted correctly. |

### Objective

Data is information represented in a form that a computer can store, process, and communicate.
