import sys

message = sys.argv

def hash_it(message):
    digest = []
    for i in message:
        digest[i] = ( (129 * message[i]) XOR message[i - 1]) % 256
