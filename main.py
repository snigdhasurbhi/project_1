#importing spy_details.py file
from spy_details import spy
from start_chat import start_chat
import re
from colorama import Fore,init
#importing start_chat.p
print 'Let\'s get started'
question = "Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?"
existing = raw_input(question)
# validating user input

#TO CHECK WHETHER THE USER WANTS TO CONTINUE AS DEFAULT USER OR NOT
if existing == "Y" or existing == "y":
    spy_name = spy["salutation"] + " " + spy["name"]
    start_chat(spy["name"], spy["age"], spy["rating"], spy["status"])
elif (existing == "N" or existing == "n"):
    spy["name"] = raw_input("What is your name?") # raw_input(): function that returns string only
    # validating user's input
    # to check whether spy has input some name or not
    if len(spy["name"]) > 0: # Start writing from here now. See how this is under the if statement?

        # regular expression which matches only alphabets
        pattern1 = '^[a-zA-Z\s]+$'
        if re.match(pattern1, spy["name"]) is not None:
            print " valid spy_name INPUT "
            # string matched

            spy["salutation"] = raw_input("What should we call you Mr. or Ms?")
            pattern2 = '^[M][r s]$'
            if re.match(pattern2, spy["salutation"]) is not None:
                print "checking...."
                spy["name"] = spy["salutation"] + " " + spy["name"]
                print 'Welcome ' + spy["name"] + '. Glad to have you back with us.'

                spy["age"] = int(raw_input("Enter your age here: "))  # int() : used for typecasting string into int
                pattern3 = '^[0-9]+$'
                if re.match(pattern3, spy["age"]) is not None:
                    print "CHECKING..."

                if spy["age"] > 12 and spy["age"] < 50:
                    print "You are good to go."
                    print "Alright " + spy["name"] + ". I'd like to know a little bit more about you before we proceed..."
                    spy["rating"]= raw_input("what is your spy rating?")
                    pattern4 = '^[0-9]+\.[0-9]+$'
                    if re.match(pattern4, spy["rating"]) is not None:
                        if spy["rating"] > 4.5:
                            print Fore.GREEN +'Great ace!'
                        elif spy["rating"] > 3.5 and spy["rating"] <= 4.5:
                            print Fore.GREEN + 'You are one of the good ones.'
                        elif spy["rating"] >= 2.5 and spy["rating"] <= 3.5:
                            print 'You can always do better'

                        spy_status = True

                        # starting chat application
                        start_chat(spy["name"], spy["age"], spy["rating"], spy["status"])
                        print Fore.GREEN + "Authentication complete. Welcome " + spy["name"] +" age: " + str(spy["age"]) + " and rating of: " +str(spy["rating"]) + " Proud to have you onboard."
                    else:
                        print Fore.RED + "Enter valid spy rating"
                        # starting chat application
                else:
                    print Fore.RED + "you do not match the age criteria."
            else:
                print Fore.RED +"enter suitable salutation"
        else:
            print Fore.RED +"enter valid name"
    else:
        print Fore.RED + "A spy needs to have valid name.Try again."
else:
    print Fore.RED +"wrong choice. Try again please."



