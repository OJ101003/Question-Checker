# Function to return a boolean that is true if a question mark is found in the userInput variable
def questionChecker(userInput):
    return "?" in userInput
#Gets user input and stores it in a variable
userInput = input("Put in the sentence.\n")
# Uses the function to find if there is a question mark in the user inputted sentence and prints a statement accordingly
if questionChecker(userInput):
    print("Statement is a question.")
else:
    print("Statement is not a question.")
