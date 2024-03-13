from base_algorithm import Algorithm

class VigenereAlgorithm(Algorithm):

    def __init__(self, key):
        self.key = key
        self.matrix = self.generateMatrix()

    def generateMatrix(self):
        matrix = []
        for i in range(26):
            lst = []
            for j in range(i, 26 + i):
                j = j % 26
                lst.append(chr(ord("a") + j))
            matrix.append(lst)
        # for row in matrix:
        #     print(row)
        return matrix

    def extendKey(self, message):
        newKey = ""
        while(len(newKey) < len(message)):
            newKey += self.key
        newKey = "".join([newKey[i] for i in range(len(message))])
        # print(newKey)
        return newKey

    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        self.key = self.extendKey(originalMessage)
        encryptedMessage = ""
        for c in range(len(originalMessage)):
            row = ord(self.key[c]) - ord("a")
            col = ord(originalMessage[c]) - ord("a")
            encryptedMessage += self.matrix[row][col]
        return encryptedMessage

    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        decryptedMessage = ""
        for c in range(len(encryptedMessage)):
            symbol = encryptedMessage[c]
            row = ord(self.key[c]) - ord("a")
            col = ((ord(symbol) - ord("a")) - row) % 26
            decryptedMessage += chr(col + ord("a"))
        return decryptedMessage

def main():
    va = VigenereAlgorithm("deceptivedeceptivedeceptive")
    encryptedMessage = va.encryptMessage("wearediscoveredsaveyourself")
    print("Encrypted Message: ", encryptedMessage)
    decryptedMessage = va.decryptMessage(encryptedMessage)
    print("Decrypted Message: ", decryptedMessage)

if __name__ == '__main__':
    main()