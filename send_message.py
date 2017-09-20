from steganography.steganography import Steganography
from select_friend import select_friend
from datetime import datetime
from globall import friends
from colorama import Fore, init
from main import spyinfo
#import spy_info_class
init()
# saving the messages
class New_Chat :
    message = ''
    time = datetime.now()
    sent_by_me = True


def send_message():
    chat_obj = New_Chat()
    friend_choice = select_friend()
    # prepare the messsage
    original_image = raw_input("What is the name of the image?")
    output_path =  raw_input("Provide name of the output image : ")
    text = raw_input("What do you want to say?")
    # Encrypting the message
    Steganography.encode(original_image, output_path, text)
    # Successful message
    print "Your message is encrypted successfully"
    #save the message

    if chat_obj.message == text:

        #save message

        spyinfo.chats.append(chat_obj)
        print "secret message is ready"
    else:
        print"wrong choice"
