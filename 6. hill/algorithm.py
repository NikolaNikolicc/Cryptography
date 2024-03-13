from base_algorithm import Algorithm
import numpy as np

class HillAlgorithm(Algorithm):

    def __init__(self, keyMatrix):
        self.keyMatrix = keyMatrix

    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        encryptedMessage = ""
        originalMessageList = [ord(ch) - ord("a") for ch in originalMessage]
        for c in range(len(originalMessage)):
            sum = 0
            for c1 in range(len(originalMessage)):
                sum += originalMessageList[c1] * self.keyMatrix[c1][c]
            encryptedMessage += chr(sum % 26 + ord("a"))
        return encryptedMessage


    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)

def main():
    key = [[3, 25, 4],[23, 6, 15],[13, 17, 21]]
    ha = HillAlgorithm(key)
    encryptedMessage = ha.encryptMessage("you")
    print("Encrypted Message: ", encryptedMessage)
    decryptedMessage = ha.decryptMessage(encryptedMessage)
    print("Decrypted message: ", decryptedMessage)

if __name__ == '__main__':
    main()