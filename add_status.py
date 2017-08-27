def add_status(current_status_message):

  if current_status_message != None:
    print "Your current status message is " + current_status_message + "\n"
  else:
    print 'You don\'t have any status message currently \n'

default = raw_input("Do you want to select from the older status (y/n)? ")