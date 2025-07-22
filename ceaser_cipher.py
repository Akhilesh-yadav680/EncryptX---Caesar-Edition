# ceaser_cipher.py

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def ceaser(original_text, shift_number, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_number
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    return output_text
