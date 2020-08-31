import string
alphabet = ' ' + string.ascii_lowercase

positions = {i:alphabet[i] for i in range(0,27)}
print(positions)

message = "hi my name is caesar"

def caesar(message, key):
    # return the encoded message as a single string!
    alphabet_len = len(alphabet)
    encoded_message = {alphabet[i]:((i + key) % alphabet_len) for i in range(alphabet_len)}
    return ''.join([alphabet[encoded_message[letter]] for letter in message])
    
encoded_message = caesar(message, 1)

print(encoded_message)

message = "hi my name is caesar"

def caesar(message, key):
    # return the encoded message as a single string!
    alphabet_len = len(alphabet)
    encoded_message = {alphabet[i]:((i + key) % alphabet_len) for i in range(alphabet_len)}
    return ''.join([alphabet[encoded_message[letter]] for letter in message])
    
encoded_message = caesar(message, 3)

print(encoded_message)

decoded_message = caesar(encoded_message, -3)
print(decoded_message)