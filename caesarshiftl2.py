#Caesar Cipher left shift 2

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) - shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result
