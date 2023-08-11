from day8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = "encode"
print(logo)


def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            end_text += alphabet[(position + shift_amount) % 26]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

should_end = True

while should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    wanna_continue = input("type 'yes' if you want to go again, otherwise type 'no'\n")
    if wanna_continue == "no":
        print("Goodbye")
        should_end = False