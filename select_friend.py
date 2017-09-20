import re
from globall import friends
from globall import friends
from colorama import init, Fore
init()
def select_friend():
    counter = 1   #to increase the counter for printing friend from friends
    for friend in friends :
        print str(counter) + ". " + friend["name"] + "Age : " + str(friend["age"])
        counter = counter + 1

    result = int(raw_input("Select from the list : "))
    pattern19 = "^[0-9]+$"
    if re.match(pattern19, result, flags=0) != None:
        if (result > 0 and result < counter):
            return result - 1
        else:
            return None
    else:
        print "Input INTEGER VALUE "

