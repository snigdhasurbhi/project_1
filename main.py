
print "Let's get started!"
spy_name = raw_input("Provide your name here :")

# chek wether spy has input something or not
if len(spy_name) > 0 :
    #code block if the condition is true.
    #concatination of salutation and name.
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    spy_slautation = raw_input("What should we call you (Mr. or Ms.)? : ")
    spy_age = raw_input("Enter your age. ?")
    print type(spy_age)
    spy_age = int(spy_age)
    print type(spy_age)
    spy_name = spy_slautation + " " + spy_name
    print "Welcome " + spy_name + " Glad to have you back with us."

    print "Alright " + spy_name + " I'd like to know a little bit more about you before we proceed..."
else:
    print "Invalid name. Try again."