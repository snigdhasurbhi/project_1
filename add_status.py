#import statements
from globall import STATUS_MESSAGE


#UPDATED STATUS MESSAGE
updated_status_message = None

def add_status(current_status_message):
    if current_status_message is not None:

        print "Your current status message is " % current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    # Ask user for choosing from older messages.
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        # validating user input
        if len(new_status_message) > 0:
        # Adding new status to the list
            STATUS_MESSAGE.append(new_status_message)
            updated_status_message = new_status_message
            print "Your updated status message is %s" % (updated_status_message)
        else:
            print "You did not provide any status message"

    elif default.upper() == 'Y':
        #Counter for serial number of messages
            item_position = 1

        # printing all older messages
            for message in STATUS_MESSAGE:
                print '%d %s' % (item_position, message)
                item_position = item_position + 1

            # asking user's choice.
            message_selection = int(raw_input("\n Choose from the above messages "))

            if len(STATUS_MESSAGE) >= message_selection:
                updated_status_message = STATUS_MESSAGE[message_selection -1]
                print  "your udated message is: " +  updated_status_message
            else:
                 print'Invalid choice. Try again.'
    else:
        print 'The option you chose is Invalid.'

    return updated_status_message
