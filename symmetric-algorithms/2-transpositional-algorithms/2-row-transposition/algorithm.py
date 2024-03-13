from base_algorithm import Algorithm
import random
import copy
import math
class RowTranspositionalAlgorithm(Algorithm):

    def __init__(self, length):
        self.length = length
        self.positions = [pos for pos in range(length)]
        random.shuffle(self.positions)

    def splitMessage(self, originalMessage):
        splittedMessage = []
        for i in range(0, len(originalMessage), self.length):
            if(i + self.length > len(originalMessage)):
                splittedMessage.append([ch for ch in originalMessage[i:]])
            else:
                splittedMessage.append([ch for ch in originalMessage[i:i + self.length]])
        return splittedMessage

    def shuffleMessage(self, splittedMessage):
        final = copy.deepcopy(splittedMessage)
        # print(self.positions)
        for index in range(len(self.positions)):
            pos = self.positions[index]
            for commonIndex in range(len(splittedMessage)):
                final[commonIndex][pos] = splittedMessage[commonIndex][index]
        # print(final)
        return final

    def undoShuffle(self, splittedMessage):
        final = copy.deepcopy(splittedMessage)
        # print(self.positions)
        for index in range(len(self.positions)):
            pos = self.positions[index]
            for commonIndex in range(len(splittedMessage)):
                final[commonIndex][index] = splittedMessage[commonIndex][pos]
        # print(final)
        return final

    def getEncryptedMessage(self, shuffledMessage):
        encryptedMessage = ""
        for i in range(len(shuffledMessage[0])):
            for j in range(len(shuffledMessage)):
                encryptedMessage += shuffledMessage[j][i]
        return encryptedMessage

    def undoEncryption(self, encryptedMessage):
        # get the same structure
        numberOfLists = math.ceil(len(encryptedMessage) / self.length)
        shuffledMessage = [[] for _ in range(numberOfLists)]
        cnt = 0
        for i in range(len(encryptedMessage)):
            shuffledMessage[cnt % numberOfLists].append(encryptedMessage[i])
            cnt += 1
        return shuffledMessage
    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        splittedMessage = self.splitMessage(originalMessage)
        # print(splittedMessage)
        shuffledMessage = self.shuffleMessage(splittedMessage)
        # print(shuffledMessage)
        encryptedMessage = self.getEncryptedMessage(shuffledMessage)
        # print(encryptedMessage)
        return encryptedMessage


    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        splittedMessage = self.undoEncryption(encryptedMessage)
        # print(splittedMessage)
        # print(self.positions)
        decryptedSplittedMessage = self.undoShuffle(splittedMessage)
        # print(decryptedSplittedMessage)
        return "".join([item for sublist in decryptedSplittedMessage for item in sublist])

def main():
    rta = RowTranspositionalAlgorithm(7)
    originalMessage = "zanimljivainformacija"
    encryptedMessage = rta.encryptMessage(originalMessage)
    print("Encrypted Message: ", encryptedMessage)
    decryptedMessage = rta.decryptMessage(encryptedMessage)
    print("Decrypted Message: ", decryptedMessage)

if __name__ == "__main__":
    main()