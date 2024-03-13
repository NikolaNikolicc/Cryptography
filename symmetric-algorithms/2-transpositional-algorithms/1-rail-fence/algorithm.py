from base_algorithm import Algorithm
import math

class RailFenceAlgorithm(Algorithm):

    def __init__(self, numOfRows):
        self.numOfRows = numOfRows
        self.rows = [[] for _ in range(self.numOfRows)]

    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        cnt = 0
        down = True
        for ch in originalMessage:
            self.rows[cnt % self.numOfRows].append(ch)
            if(cnt == self.numOfRows - 1):
                down = False
            elif(cnt == 0):
                down = True
            if(down):
                cnt += 1
            else:
                cnt -= 1
        encryptedMessage = ""
        for row in self.rows:
            encryptedMessage += "".join(row)
        for row in self.rows:
            print(row)
        return encryptedMessage

    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        r = [[] for _ in range(self.numOfRows)]
        cnt = 0
        down = True
        for ch in encryptedMessage:
            r[cnt % self.numOfRows].append(ch)
            if (cnt == self.numOfRows - 1):
                down = False
            elif (cnt == 0):
                down = True
            if (down):
                cnt += 1
            else:
                cnt -= 1
        numberOfRows = []
        for row in r:
            numberOfRows.append(len(row))
        newRows = []
        prev = 0
        for num in numberOfRows:
            newRows.append([ch for ch in encryptedMessage[prev:prev + num]])
            prev += num
        decryptedMessage = ""
        cnt = 0
        down = True
        while(len(decryptedMessage) != len(encryptedMessage)):
            decryptedMessage += newRows[cnt % self.numOfRows].pop(0)
            if (cnt == self.numOfRows - 1):
                down = False
            elif (cnt == 0):
                down = True
            if (down):
                cnt += 1
            else:
                cnt -= 1
        return decryptedMessage


def main():
    rfa = RailFenceAlgorithm(3)
    originalMessage = "napadamoupodneakonebudevetra"
    encrypetMessage = rfa.encryptMessage(originalMessage)
    print("Encrypted message: ", encrypetMessage)
    print(len(originalMessage))
    decryptedMessage = rfa.decryptMessage(encrypetMessage)
    print("Decrypted message: ", decryptedMessage)

if __name__ == "__main__":
    main()