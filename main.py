print 'Let\'s get started'

spy_name = raw_input("What is your name?")

if len(spy_name) > 0:
# Start writing from here now. See how this is under the if statement?


    print 'Welcome ' + spy_name + '. Glad to have you back with us.'

    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")

    spy_name = spy_salutation + " " + spy_name

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = int(raw_input("What is your age?"))
    if spy_age > 12 and spy_age <50 :
        print  "you are good to go"
        spy_rating= int(raw_input("what is your spy rating?"))
        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'

        else:
            print 'We can always use somebody to help in the office.'
        spy_is_online = True

        print "Authentication complete. Welcome " + spy_name +" age: " + str(spy_age) + " and rating of: " +str(spy_rating) + " Proud to have you onboard"



    else:
        print "you do not match the age criteria"
else:
    print "A spy needs to have a valid name. Try again please."



