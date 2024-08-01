# Simple-Cypher
Cesar and Vignére code cipher and decryptor

# Usage


### Cesar Encrypt example
```
Message = "Hello everyone"
Cipher = CesarCypher(Message)
NewMessage = Cipher.CsEncrypt(3) # This argument in numbers means the number of characters shifted. In this case, "3" is recommended.
print("Your Cesar code: ",NewMessage)
```

### Cesar Decrypt example
```
Message2 = "Krod d wrgrv"
Cipher2 = CesarCypher(Message2)
NewMessage2 = Cipher2.CsDecrypt(3) # This argument in numbers means the number of characters shifted. In this case, "3" is recommended.
print("Your Caesar code decrypted: ",NewMessage2)
```

### Vigenére Encrypt example
```
Message3 = "Goodbye everyone"
Key = "BYE"
Cipher3 = VigenereCypher(Message3)
NewMessage3 = Cipher3.VigEncrypt(Message3, Key)
print("Your Vigenere code:", NewMessage3)
```

### Vigenére Decrypt example
```
Message4 = "Agqck d hgdra"
Key2 = "BYE"
Cipher4 = VigenereCypher(Message4)
NewMessage4 = Cipher4.VigDecrypt(Message4, Key2)
print("Your Vigenere code decrypted: ",NewMessage4)
```

# Notes
I can't upload this file to pypi (for now), but I will soon, Meanwhile the file is only available here.

# AUTHOR
Ēn0røøD 