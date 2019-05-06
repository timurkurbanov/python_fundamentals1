#How would you calculate a good tip for a 55 dollar meal? Use print to print the answer.
#Steps: 1 - ask the user the bill value
#Steps: 2 - user gives the value
#Step: 3 - calculate the tip from the bill
#Step: 4 - display the tip


print ("What is the amount of the bill?")
bill = input()
tip = (int(bill) * 0.15)
print (tip)

#Try adding a string and an integer with the + operator. What happens? Find a way to convert the integer into a string first and use print to print the result.
print(str(99)+ " bottles of beer")

#Try outputting the result of 45628 multiplied by 7839 in a sentence by using string interpolation.

"Result of multiplication 45628 and 7839 {}".format(45628 * 7839)
