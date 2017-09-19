from steganography.steganography import Steganography
import select_friend
from datetime import datetime
from globall import friends


def send_message():
    friend_choice = select_friend()
    # prepare the messsage
    original_image = raw_input("What is the name of the image?")
    output_path = 'smm.jpg'
    text = raw_input("What do you want to say?")
    # Encrypting the messag
    Steganography.encode(original_image, output_path, text)
    # Successful message
    print "Your message is encrypted successfully"
    #save the message
    new_chat = {"messaage": text, "time ": datetime.now(), "sent_by_me": True

    }
    friends[friend_choice]['chats'].append(new_chat)
    print "secret message is ready"
