cardKey, doorKey = 3248366, 4738476

def getEncryptionKey(publicKey, otherPublicKey):
    loops, value, subject, modulo = 0, 1, 7, 20201227
    while value != publicKey:
        value = (value * subject) % modulo
        loops += 1
    return pow(otherPublicKey, loops, modulo)

print(getEncryptionKey(cardKey, doorKey))
print(getEncryptionKey(doorKey, cardKey))
