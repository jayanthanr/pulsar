name = input("What is your name? ")
#print("Hello " + name)
# Removing white spaces from the input
name = name.strip()
#print("Hello,",name)
# Init cap the name while printing
#name = name.capitalize()
#print("Hello,",name)
# capitalize all the words in the name
name = name.title()
# Strip of white space and Init cap all the words
#name = name.strip().title()
# can actually have all the methods called at once to avoid lines of code but might be not elegant
#name = input("What is your name? ").strip().title()
print("Hello,",name)
# Splitting input into multiple variables for print is also possible
first_name, last_name = name.split(" ")
#
print("Hello,",first_name,"with surname",last_name)
