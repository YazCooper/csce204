#author yaz c


encode_map = {
    "a":"p",
    "b":"q",
    "c":"r",
    "d":"s",
    "e":"t",
    "f":"u",
    "g":"v",
    "h":"w",
    "i":"x",
    "j":"y",
    "k":"z",
    "l":"a",
    "m":"b",
    "n":"c",
    "o":"d",
    "p":"e",
    "q":"f",
    "r":"g",
    "s":"h",
    "t":"i",
    "u":"j",
    "v":"k",
    "w":"l",
    "x":"m",
    "y":"n",
    "z":"o", 
    " ": " "
}


decode_map = {encode_map[k] : k for k in encode_map}

def encode(message):
    mess=" "
    for let in message:
        if let.lower() in encode_map:
            mess += encode_map[let.lower()]
        
        
        
    return mess 





def to_letters(symbols):
    mess=" "
    for let in symbols:
        if let.lower() in decode_map:
            mess += decode_map[let.lower()]
    return mess

print("Secret Messages!")

while True:
    
    message = input("(E)ncode, (D)ecode,(Q)uit: ").lower()

    if message == "e":
        asks = input("Enter a secret message: ").lower()
        command = encode(asks)
        print(f"Your encoded message is: {command}",sep='',)
    elif message == "d":
        ask = input("Enter an encoded message: ").lower()
        types = to_letters(ask)
        print(f"Your decoded message is : {types}")
    elif message == "q":
        break
    else:
        print("Invalid Input")