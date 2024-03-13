from base_algorithm import Algorithm

class VernamAlgorithm(Algorithm):

    def __init__(self, key):
        self.key = key

    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        encryptedMessage = ""
        for c in range(len(self.key)):
            encryptedMessage += str(int(originalMessage[c]) ^ int(self.key[c]))
        return encryptedMessage

    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        decryptedMessage = ""
        for c in range(len(self.key)):
            decryptedMessage += str(int(encryptedMessage[c]) ^ int(self.key[c]))
        return decryptedMessage

def main():
    va = VernamAlgorithm("10100001")
    encryptedMessage = va.encryptMessage(   "11110000")
    print("Encrypted Message: ", encryptedMessage)
    decryptedMessage = va.decryptMessage(encryptedMessage)
    print("Decrypted Message: ", decryptedMessage)

if __name__ == '__main__':
    main()