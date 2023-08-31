alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt ,Type 'decode' to decrypt :" ).lower()
text= input("Type Your Message : ").lower()
shift=int(input("Type The Shift Number :"))
shift = shift % 26

def caesar(start_text, shift_amount, cipher_drection):
    end_text = ""
    if cipher_drection == 'decode':
            shift_amount *= -1
    for letter in start_text:
        position=alphabet.index(letter)
        new_positon= position+shift_amount
        new_text= alphabet[new_positon]
        end_text += new_text
    print(end_text)


caesar(start_text=text, shift_amount=shift, cipher_drection=direction)

# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_positon= position+shift_amount
#         new_text= alphabet[new_positon]
#         cipher_text += new_text
#     print(f"The Encode text is {cipher_text} ")


# def decrypt(cipher_text,shift_amount):
#     org_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_positon= position-shift_amount
#         new_text= alphabet[new_positon]
#         org_text += new_text
#     print(f"The Decode text is {org_text}")


# if direction == 'encode':
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text,shift_amount=shift)
# else:
#     print("invalid choice")

# rewrite code for reduce Time complexity