alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift_amount) % len(alphabet)
#             cipher_text += alphabet[new_position]
#         else:
#             cipher_text += letter
#     return cipher_text

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position - shift_amount) % len(alphabet)
#             plain_text += alphabet[new_position]
#         else:
#             plain_text += letter
#     return plain_text


# Function call
# if direction == "encode":
#     print(f"Encrypted message: {encrypt(text, shift)}")
# elif direction == "decode":
#     print(f"Decrypted message: {decrypt(text, shift)}")
# else:
#     print("Invalid direction. Please type 'encode' or 'decode'.")


def caesar(cipher_text, shift_amount, direction_which):
    plain_text = ""

    # Flip the shift once if decoding
    if direction_which == "decode":
        shift_amount *= -1

    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    return plain_text

go_again = True

while go_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()
    text = input("Message: ").strip().lower()
    shift = int(input("Shift number: "))
    
    print(f"{caesar(text, shift, direction)}")
    
    go_again = input("Do you want to go again? Type 'yes' or 'no' : ").lower()
    
    if go_again == "no":
        go_again = False
    