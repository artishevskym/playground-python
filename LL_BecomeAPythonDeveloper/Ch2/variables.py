# 
# Learning - variables
#

# Declare a variable and initialize it
f = 0
print (f)

# Re-declaring the variables works
f = "abs"
print (f)

# Error: variables of different types cannot be combined
# print("string " + 123)
print("string " + str(123))

# Global vs local variables in functions
def someFunction():
    # local f
    f = "def"
    print (f)

# print local variable
someFunction()
# print global variable
print (f)

del f
# Error: f is not defined
# print (f)