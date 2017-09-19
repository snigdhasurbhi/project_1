#IMPORTING TWO FILES HERE
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from globall import friends
from colorama import Fore,init
import time
from read_chat_history import read_chat_history

#start_chat() function definition
def start_chat(name, age, rating, status):
    from globall import current_status_message
    # validating user's details
    error_message = None  # variable for storing error message
    if not (age > 12 and age < 50):
        error_message = " INVALID AGE. PROVIDE VALID AGE"
        print error_message
    else:
        welcome_message = Fore.BLUE + "AUTHENTICATION COMPLETED. Welcome\n  " +\
                          Fore.BLUE + "Name : " + name + "\n" +\
                          Fore.BLUE + "Age : " + str(age) + "\ n" + \
                          Fore.BLUE + "\Rating: " + str(rating) + "\n " + \
                          Fore.GREEN + "Proud to have you here"
        print welcome_message

        # displaying menu for user
        show_menu = True
        while show_menu:
            time.sleep(1)
            menu_choices = " What do you want to do ? \n" \
                               " 1. ADD STATUS \n " \
                               " 2.ADD A FRIEND \n" \
                               " 3.SEND A SECRET MESSAGE \n" \
                               " 4.READ A SECRET MESSAGE \n" \
                               " 5.READ CHATS FROM A USER \n" \
                               " 6. CLOSE APPLICATION \n"

            result = int(raw_input(menu_choices))

            # validating user input
            if (result == 1):
                time.sleep(1)
                current_status_message = add_status(current_status_message)
                time.sleep(1)
            elif (result == 2):
                time.sleep(1)
                number_of_friends = add_friend()
                print "You have %d friends" % (number_of_friends)
            elif (result == 3):
                time.sleep(1)
                send_message()
            elif (result == 4):
                time.sleep(1)
                read_message()
            elif result == 5:
                time.sleep(1)
                read_chat_history()
            elif (result == 6):
                    # close application
                    show_menu = False

                    time.sleep(1)
                    print Fore.RED + "Application is closed now."
            else:
                print "wrong choice.Try again later."