#import statements
from globall import friends
import re
# importing spy_details.py file

import re
from globall import friends
from colorama import Fore,init
from spy_inform_class import Spy_Info


#ADD NEW FRIENDS
def add_friend():
    friend_obj =Spy_Info("Mr.", "guest", 30, 2.5, True )
    friend_obj.name =raw_input("add your friends name :")
    if len(friend_obj.name) > 0:
        # regular expression which matches only alphabets
        pattern5 = '^[a-zA-Z\s]+$'
        if re.match(pattern5, friend_obj.name) is not None:
         # string matched
            friend_obj.salutation = raw_input("Are they Mr or Ms ? ")
            pattern6 = '^[M][r s]$'
            if re.match(pattern6, friend_obj.salutation) is not None:
                print "Checking .."
                #concatination
                friend_obj.name =  friend_obj.salutation + " " + friend_obj.name
                friend_obj.age =int (raw_input("Age? "))
                pattern7 = '^[0-9]+$'
                if re.match(pattern7, friend_obj.age) is not None:
                    print "CHECKING..."
                    friend_obj.rating=  raw_input(" Spy Rating")
                    pattern8 = '^[0-9]+\.[0-9]+$'
                    if re.match(pattern8, friend_obj.rating) is not None:
                        print "CHECKING.."
                    #users input validation
                    if len(friend_obj.name > 0 and friend_obj.age > 12 and  friend_obj.age < 50):
                        # ADDFRIEND
                        friends.append(friend_obj)
                        print"friend is added!"
                        return len(friends)

                    else:
                        print " Sorry! Invalid entry. We cant add spy with the details you provided"
                else:
                    print "Input friend's age format is not valid"
            else:
                print "Input friend salutation's format is not valid. "
        else:
            print "Input friend name's format  is not valid"
    else:
        print "Enter valid name to continue "