#importing spy_details.py file
from spy_details import spy
from start_chat  import start_chat


#importing start_chat.p


print 'Let\'s get started'

question = "Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?"
existing = raw_input(question)
# validating user input

#TO CHECK WHETHER THE USER WANTS TO CONTINUE AS DEFAULT USER OR NOT
if existing == "Y" or existing == "y":
   spy_name = spy["salutation"] + " " + spy["name"]
   start_chat(spy["name"], spy["age"], spy["rating"], spy["is_online"])
elif (existing == "N" or existing == "n"):
    spy["name"] = raw_input("What is your name?")
    if len(spy["name"]) > 0: # Start writing from here now. See how this is under the if statement?
        if not spy["name"].isalpha():
            print " invalid spy_name INPUT "
            spy["name"] = raw_input("provide your name here again :")
        else:
            print "VALID INPUT NAME "
            spy["salutation"] = raw_input("What should we call you Mr. or Ms?")
            spy["name"] = spy["salutation"] + " " + spy["name"]
            print 'Welcome ' + spy["name"] + '. Glad to have you back with us.'
            while True:
                try:
                    spy["age"] = int(raw_input("Enter your age here: "))  # int() : used for typecasting string into int

                except ValueError:
                    print "enter valid age. Try again."
                if spy["age"] > 12 and spy["age"] < 50:
                    print "You are good to go."
                 print "Alright " + spy["name"] + ". I'd like to know a little bit more about you before we proceed..."
                spy["rating"]= raw_input("what is your spy rating?")
                if spy["rating"] > 4.5:
                    print 'Great ace!'
                elif spy["rating"] > 3.5 and spy["rating"] <= 4.5:
                    print 'You are one of the good ones.'
                elif spy["rating"] >= 2.5 and spy["rating"] <= 3.5:
                    print 'You can always do better'
                else:
                    print 'We can always use somebody to help in the office.'
                    spy_is_online = True

                    # starting chat application
                    start_chat(spy["name"], spy["age"], spy["rating"], spy["is_online"])
                    print "Authentication complete. Welcome " + spy["name"] +" age: " + str(spy["age"]) + " and rating of: " +str(spy["rating"]) + " Proud to have you onboard."

                    # starting chat application
            else:
                  print "you do not match the age criteria."
    else:
        print "A spy needs to have valid name.Try again."
else:
    print "wrong choice. Try again please."



