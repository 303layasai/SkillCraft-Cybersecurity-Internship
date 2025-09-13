"""
SkillCraft Technology Internship
Task 02 - Image Encryption Tool using Pixel Manipulation
Developed by: Laya Sai
"""

from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    arr = np.array(img)
    encrypted_arr = arr ^ key
    encrypted_img = Image.fromarray(encrypted_arr)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    arr = np.array(img)
    decrypted_arr = arr ^ key
    decrypted_img = Image.fromarray(decrypted_arr)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    # Example paths - change if you like
    input_file = "sample.png"
    encrypted_file = "encrypted.png"
    decrypted_file = "decrypted.png"
    key_value = 123

    print("SkillCraft Task 02 - Image Encryption")
    print("Developer: Laya Sai\n")

    # encrypt -> decrypt (example run)
    encrypt_image(input_file, encrypted_file, key=key_value)
    decrypt_image(encrypted_file, decrypted_file, key=key_value)
