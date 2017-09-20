from steganography.steganography import Steganography
from select_friend import select_friend
from globall import friends
from datetime import datetime
from send_message import New_chat
def read_message():
    #choose friends from list
    sender = select_friend()
    chat_obj = New_chat()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print secret_text
    chat_obj.message =  secret_message
    chat_obj.sent_by_me = False
    friends[sender].chats.append(chat_obj)
    print "Your secret message has been saved!"