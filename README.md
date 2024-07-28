# Simple-Cypher
Cesar and Vignére code cipher and decryptor

# Cesar Encrypt
Message = "Hello everyone"
Cipher = CesarCypher(Message)
NewMessage = Cipher.CsEncrypt(3)
print("Your Cesar code: ",NewMessage)

# Cesar Decrypt
Message2 = "Krod d wrgrv"
Cipher2 = CesarCypher(Message2)
NewMessage2 = Cipher2.CsDecrypt(3)
print("Your Caesar code decrypted: ",NewMessage2)

# Vigenére Encrypt
Message3 = "Goodbye everyone"
Key = "BYE"
Cipher3 = VigenereCypher(Message3)
NewMessage3 = Cipher3.VigEncrypt(Message3, Key)
print("Your Vigenere code:", NewMessage3)

# Vigenére Decrypt
Message4 = "Agqck d hgdra"
Key2 = "BYE"
Cipher4 = VigenereCypher(Message4)
NewMessage4 = Cipher4.VigDecrypt(Message4, Key2)
print("Your Vigenere code decrypted: ",NewMessage4)
