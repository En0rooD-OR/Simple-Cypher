# Simple-Cypher
Cesar and Vignére code cipher and decryptor

# Usage

### Caesar Cipher and Decipher

#### Caesar Cipher
The Caesar cipher shifts each letter in the message by a fixed number of positions in the alphabet. For example, a shift of 3 turns "A" into "D".

**Usage Example:**
```
Message = "Hello everyone"
Cipher = CesarCypher(Message)
NewMessage = Cipher.CsEncrypt(3) # Shifts each letter by 3 positions
print("Your Caesar code: ", NewMessage)
```

#### Caesar Decipher
The Caesar decipher reverses the cipher process, shifting each letter in the encrypted message back by the same number of positions.

**Usage Example:**
```
Message2 = "Krod d wrgrv"
Cipher2 = CesarCypher(Message2)
NewMessage2 = Cipher2.CsDecrypt(3) # Shifts each letter back by 3 positions
print("Your Caesar code decrypted: ", NewMessage2)
```

### Vigenère Cipher and Decipher

#### Vigenère Cipher
The Vigenère cipher uses a keyword to determine the shift for each letter in the message. Each letter of the keyword corresponds to a different shift.

**Usage Example:**
```
Message3 = "Goodbye everyone"
Key = "BYE"
Cipher3 = VigenereCypher(Message3)
NewMessage3 = Cipher3.VigEncrypt(Message3, Key)
print("Your Vigenère code: ", NewMessage3)
```

#### Vigenère Decipher
The Vigenère decipher reverses the cipher process using the same keyword to revert the shift for each letter in the encrypted message.

**Usage Example:**
```
Message4 = "Agqck d hgdra"
Key2 = "BYE"
Cipher4 = VigenereCypher(Message4)
NewMessage4 = Cipher4.VigDecrypt(Message4, Key2)
print("Your Vigenère code decrypted: ", NewMessage4)
```

# Notes
I can't upload this file to pypi (for now), but I will soon, Meanwhile the file is only available here.

**Author**
[Ēn0røøD](https://youtube.com/@en0roodor?si=MK6lOlsDk4TXlVAT)