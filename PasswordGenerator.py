#first import random and string 
#we import string so we can grab all the lower and uppercase numbers digits everything

import random
import string

#first we will ask the user what the minimum length is and what kind of characters
def generate_password(min_length, numbers=True, special_character=True):
    #what these are is basically all the upper and lower letters
    letters = string.ascii_letters
    #this is all the numbers
    digits = string.digits
    #this is all the special characters
    special = string.punctuation

    #this is here because we will always have letters
    characters = letters
    #if numbers is true then we will add it to the letters stirng
    if numbers:
        characters += digits
    #same thign ehre we will add it to the letter string
    if special_character:
        characters += special

    #emptry pwd string
    pwd = ""
    #for now it will be set to false until it meets all requirements
    meets_criteria = False
    has_number = False
    has_special = False
    
    #while we not have special or a number or the length is not equal to the min length
    while not meets_criteria or  len(pwd) < min_length:
        #here this new character will pick a new letter
        new_char = random.choice(characters)
        #add this to password
        pwd += new_char

        #if our new char is in digits then has number will be true now and special
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        #if we have a number this will equal true if we dont its false
        if numbers:
            meets_criteria = has_number
        #so whether it is true or false then we check for special characters
        # we use the and because if numbe was false then it doesnt meet criteria it will return false 
        #so having 2 trues will be true and having a false and true is false
        if special_character:
            meets_criteria = meets_criteria and has_special

    #now it will have everything
    return pwd

#here is user info
#we need an int number
min_length = int(input("Enter Minimum Length: "))
#we need a yes for it to be true so if they enter anyhting like Y or Y its true anythign else is false
has_number = input("Do you want to have numbers?(y/n): ").lower() == "y"
has_special = input("Do you want to have characters?(y/n): ").lower() == "y"


#call the function 
pwd = generate_password(min_length, has_number, has_special )
print("Your generated password is:", pwd)