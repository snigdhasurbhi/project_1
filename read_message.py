from steganography.steganography import Steganography
from select_friend import select_friend
from globall import friends
from datetime import datetime
def read_message():
    #choose friends from list
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print secret_text
    new_chat = {"message": secret_message, "time": datetime.now(), "sent_by_me": False

    }
    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"