# Ordered, immutable data type for text
myString1 = "Hello"         # How to create a string
myString2 = """Hello
World"""                    # How to spread a string over multiple lines, 3 " at each end
myChar1 = myString1[0]      # How to access specific character in string
myChar2 = myString1[-1]     # How to access last character, -2 for 2nd to last
# However, you cannot change values with this, myString1[0] = "h", won't work
myString3 = myString1[1:4]  # Creates string with indexes 1, 2 and 3 from myString1, not including index 4
myString3 = myString1[:4]   # Creates string made up of all indexes from myString1 up to and not including index 4
myString3 = myString1[2:]   # Creates string made of all indexes from myString1, index 2 and onwards, including index 2
myString3 = myString1[::2]  # Creates string with every second index from myString1
myString3 = myString1[::-1]     # Reverses myString1
myString4 = myString1 + myString3 + "again"   # How to concatenate strings
for i in myString1:         # How to iterate over string
    print(i)
if "ell" in myString1:      # How to check if characters are in string
    print("yes")
myString5 = myString1.strip()   # How to remove whitespace
myString5 = myString1.upper()   # How to make it uppercase
myString5.isupper()         # How to check if whole string is uppercase
myString5 = myString1.lower()   # How to make it lowercase
myString5.islower()         # How to check if whole string is uppercase
myString5.startswith("He")  # How to check if string starts with the characters given
myString5.endswith("llo")   # How to check if string ends with characters given
myString5.find("ell")        # Finds the index of the first character of the first instance of the substring
# If .find() doesn't find the substring/character, it returns -1
myString5.count("o")        # Checks how many of this character/substring exists in string
myString5 = myString5.replace("llo", "LLO")     # Replaces the specified substring with the other substring,
# myString5.replace() on its own doesn't change the original, only returns the new one
myString6 = "How are you doing"
myList1 = myString6.split()     # Separates each word into an element in the list, splits through spaces by default
myString7 = "How,are,you,doing"
myList2 = myString7.split(",")  # This does the same thing but splits with commas
myString8 = "".join(myList1)    # Combines all elements from list into 1 string, but with no spaces between words
myString8 = " ".join(myList1)   # Combines all elements from list, now with spaces in between words
# Format strings with: %, .format()

# Old Style
myVar1 = "Tom"
myString9 = "the variable is %s" % myVar1
# %s creates placeholder for an external string, and % myVar1 makes that external variable the contents of myVar1, "Tom"
# use %d for an integer, %f for a float, %.2f for a float that has 2dp

# Also Old Style
myVar2 = "Tim"
myVar3 = 6
myString10 = "the variables are {} and {}".format(myVar2, myVar3)
# {} creates a placeholder for any data type, use the .format() to state variables to insert, first variable in first {}

# New Style
myVar4 = "Toby"
myVar5 = 24
myString11 = f"the variables are {myVar4} and {myVar5}"
# uses f at start of string and put the variable names directly into the curly brackets, this is the best method
