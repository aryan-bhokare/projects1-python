alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
size = len(alphabet)

def encode(n, msg):
    cipher_text = ""
    for letter in msg:
        pos = alphabet.index(letter)
        new_pos = pos + n
        if new_pos >= size:
            new_pos = new_pos - size
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The encoded message is {cipher_text}: ")

def decode(n, mssg):
    not_cipher = ""
    for letter in mssg:
        pos1 = alphabet.index(letter)
        newpos = pos1 - n
        if newpos <= 0:
            newpos = size - newpos
        new_letter = alphabet[newpos]
        not_cipher += new_letter
    print(f"The Decoded message is {not_cipher}: ")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")
text = (input("Type your message: \n")).lower()
shift = int(input("Type the shift number: \n"))
if direction == "encode":
    encode(shift, text)
elif direction == "decode":
    decode(shift, text)
else:
    print("Inavalid input")

