#start_chat() function definition
def start_chat(name, age, rating, s):
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do ? \n 1. ADD STATUS \n 2. CLOSE APPLICATION"
        result = int(raw_input(menu_choices))

        #validating user input
        if result == 1:
            current_status_message = add_status(current_status_message)
        elif (result == 2):
            show_menu = False
        else:
             print "wrong choice.Try again later."