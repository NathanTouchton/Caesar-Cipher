from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text_input = input("Type your message:\n").lower()
shift_input = int(input("Type the shift number:\n"))
while shift_input > 26:
    shift_input = int(input("Please enter a number that is 26 or less.\n"))

def caesar(function, text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if function == "encode":
                new_posistion = position + shift
            elif function == "decode":
                new_posistion = position - shift
            new_letter = alphabet[new_posistion]
            cipher_text += new_letter
        elif letter not in alphabet:
            cipher_text += letter
    if function == "encode":
        print(f"The encoded message is {cipher_text}")
    elif function == "decode":
        print(f"The decoded message is {cipher_text}")
    restart = input("Do you want to restart the program? Type 'yes' or 'no'\n").lower()
    if restart == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text_input = input("Type your message:\n").lower()
        shift_input = int(input("Type the shift number:\n"))
        while shift_input > 26:
            shift_input = int(input("Please enter a number that is 26 or less.\n"))
        caesar(function = direction, text = text_input, shift = shift_input)

caesar(function = direction, text = text_input, shift = shift_input)