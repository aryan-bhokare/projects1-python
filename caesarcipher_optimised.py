alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
size = len(alphabet)

def caesar ( shift_amount, start_text, cipher_direction ) :
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
            if shift_amount ==0:
                shift_amount = size-1
        new_position = position + shift_amount
        if cipher_direction == "decode" and new_position <=0:
            new_position = size-new_position
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}.")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")
text = (input("Type your message: \n")).lower()
shift = int(input("Type the shift number: \n"))

caesar(shift, text, direction)
