from steganography.steganography import Steganography
from select_friend import select_friend
def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print secret_message