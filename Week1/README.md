# Week 1

## Objectives
Learn about Variables, strings, numbers and if statements.

### Variables
Variables are used when we want to save some information for use later. They are set by using `variable_name = thing_to_save`

For instance, if we wanted to save a number, we would use `mario_coins = 100`. Then we could access and update mario's coins by using the `mario_coins` variable.

### numbers
There are several kinds of numbers we can use, but for now we are only going to talk about integers. These are whole numbers (ie, no fractions or decimals).
An example of an integer is 50, 100, 75, etc.

### strings
Strings are another thing we can use. Strings are letters or words. They're denoted by using single or double quotes. 
You can save them into a variable by using `name = "fred"` or `name = 'fred'`

### if statements
If statements are used in the way it sounds. "If this is true, then do this". They're denoted by: `if <condition>:`.
The condition can be literally anything. Say Mario must have 50 coins before he can enter a door. An if statement to cover this would look like this:
```
if mario_coins > 100:
  print("ENTER DOOR")
```

Notice the body of the if statement is indented! This is how Python knows when the if statement is finished or not.
