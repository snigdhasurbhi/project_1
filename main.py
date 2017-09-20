#importing spy_details.py file
from spy_details import spy
from start_chat import start_chat
import re
from colorama import Fore, init
from spy_inform_class import Spy_Info
init()
spyinfo = Spy_Info("Mr.", "guest", 30, 2.5, True )
#importing start_chat.p
print 'Let\'s get started'
question = "Continue as " + spyinfo.get_salutation() + ". " + spyinfo.get_name() + "(Y/N)?"
existing = raw_input(question)
# validating user input

#TO CHECK WHETHER THE USER WANTS TO CONTINUE AS DEFAULT USER OR NOT
if existing == "Y" or existing == "y":
    spy_name = spy["salutation"] + " " + spy["name"]
    start_chat(spyinfo)
elif (existing == "N" or existing == "n"):
    spyinfo.name= raw_input("What is your name?") # raw_input(): function that returns string only
    # validating user's input
    # to check whether spy has input some name or not
    if len(spyinfo.name) > 0: # Start writing from here now. See how this is under the if statement?

        # regular expression which matches only alphabets
        pattern1 = '^[a-zA-Z\s]+$'
        if re.match(pattern1, spyinfo.name) is not None:
            print " valid spy_name INPUT "
            # string matched

            spyinfo.salutation = raw_input("What should we call you Mr. or Ms?")
            pattern2 = '^[M][r s]$'
            if re.match(pattern2, spyinfo.salutation) is not None:
                print "checking...."
                spyinfo.name= spyinfo.salutation+ " " + spyinfo.name
                print 'Welcome ' + spyinfo.name + '. Glad to have you back with us.'

                spyinfo.age = raw_input("Enter your age here: ")  # int() : used for typecasting string into int
                pattern3 = '^[0-9]+$'
                if re.match(pattern3, spyinfo.age) is not None:
                    print "CHECKING..."

                if spyinfo.age > 12 and spyinfo.age< 50:
                    print "You are good to go."
                    print "Alright " + spyinfo.name + ". I'd like to know a little bit more about you before we proceed..."
                    spyinfo.rating= raw_input("what is your spy rating?")
                    pattern4 = '^[0-9]+\.[0-9]+$'
                    if re.match(pattern4, spyinfo.rating) is not None:
                        if spyinfo.rating > 4.5:
                            print Fore.GREEN +'Great ace!'
                        elif spyinfo.rating> 3.5 and spyinfo.rating<= 4.5:
                            print Fore.GREEN + 'You are one of the good ones.'
                        elif spyinfo.rating >= 2.5 and spyinfo.rating<= 3.5:
                            print  Fore.CYAN + 'You can always do better'

                        spy_status = True

                        # starting chat application
                        start_chat(spyinfo)
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



