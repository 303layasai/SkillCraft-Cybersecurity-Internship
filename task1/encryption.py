def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if _name_ == "_main_":
    print("=== Caesar Cipher Program ===")
    print("Developed by: Laya Sai\n")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Message:", decrypted)
