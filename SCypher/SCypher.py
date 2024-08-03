class CesarCypher:
    def __init__(self, message):
        self.message = message

    def CsEncrypt(self, shift):
        encrypted_message = ""
        for char in self.message:
            if char.isalpha():
                shifted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
                if char.isupper():
                    shifted_char = shifted_char.upper()
                encrypted_message += shifted_char
            else:
                encrypted_message += char
        return encrypted_message
    
    def CsDecrypt(self, shift):
        decrypted_message = ""
        for char in self.message:
            if char.isalpha():
                shifted_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
                if char.isupper():
                    shifted_char = shifted_char.upper()
                decrypted_message += shifted_char
            else:
                decrypted_message += char
        return decrypted_message


class VigenereCypher:
    def __init__(self, plain_text):
        self.plain_text = plain_text

    def VigEncrypt(self, plain_text, key):
        encrypted_text = ''
        key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
        for i in range(len(plain_text)):
            if plain_text[i].isalpha():
                shift = (ord(key_repeated[i].lower()) - ord('a')) % 26
                shifted_char = chr(((ord(plain_text[i].lower()) - ord('a') + shift) % 26) + ord('a'))
                if plain_text[i].isupper():
                    shifted_char = shifted_char.upper()
                encrypted_text += shifted_char
            else:
                encrypted_text += plain_text[i]

        return encrypted_text

    def VigDecrypt(self, cipher_text, key):
        decrypted_text = ''
        key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
        for i in range(len(cipher_text)):
            if cipher_text[i].isalpha():
                shift = (ord(key_repeated[i].lower()) - ord('a')) % 26
                shifted_char = chr(((ord(cipher_text[i].lower()) - ord('a') - shift) % 26) + ord('a'))
                if cipher_text[i].isupper():
                    shifted_char = shifted_char.upper()
                decrypted_text += shifted_char
            else:
                decrypted_text += cipher_text[i]

        return decrypted_text
