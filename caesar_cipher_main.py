import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #letter list 

while True:
    response = input("Would you like to encrypt or to decrypt\n").lower()
    if response.startswith("e"):
        mode = 'encrypt'
        break
    elif response.startswith("d"):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.') 

print("-----------------------------------------------------")

while True:
    k = input(f"Please enter the key to use (0 - {len(SYMBOLS)-1})\n")
    if not k.isdecimal():
        continue
    key = int(k)
    if 0 <= key < len(SYMBOLS):
        break
    print(f"Key must be between 0 and {len(SYMBOLS)-1}")

print("-----------------------------------------------------------")		

message = input("Enter your message: ").upper()     

translated = ""	

print("----------------------------------------------------")

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num = num + key
        else:  # decrypt
            num = num - key
        num = num % len(SYMBOLS)          
        translated += SYMBOLS[num]
    else:
        translated += symbol              

print("\nYour translated message is:")
print(translated)


pyperclip.copy(translated)
print("(The result has been copied to your clipboard!)")
