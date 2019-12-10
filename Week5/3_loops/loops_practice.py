# "range(1,11)" just provides us a list of numbers 1-10 (the last number isn't included).
# The list in this case would look like this: [1,2,3,4,5,6,7,8,9,10].

# For loop
## This takes each number inside "range", and saves it as a variable "i". It does whatever is in the loop with that variable, then moves to the next number.
## In this case, the first time it goes through the loop, i is 1 (the first item in the list provided by range).
## Then it will print it, since that's the only thing inside the loop. When it's done with that, it will move to the next number: 2 and do the same thing.
## And so on and so on until it reaches 10. It will print 10 and exit the loop.
for i in range(1,11):
    print(i)

# While loop
## While loops will go on forever until whatever condition you provide turns false.
## If the condition is false at the start, the loop is never entered.
do_loop = True
while do_loop:
    user_input = input("Should I do the loop again? ")
    if user_input == 'no':
        do_loop = False
        print("Ok, exiting loop")

