from base_algorithm import Algorithm
import numpy as np
import copy
import scipy

class HillAlgorithm(Algorithm):

    def __init__(self, keyMatrix):
        self.keyMatrix = keyMatrix

    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        encryptedMessage = ""
        originalMessageList = [ord(ch) - ord("a") for ch in originalMessage]
        encryptedMessage = np.matmul(originalMessageList, self.keyMatrix)
        return encryptedMessage

    def findInverseElement(self, elem):
        elem = int(elem)
        inverse = 0
        while(True):
            if((elem * inverse) % 26 == 1):
                return inverse
            inverse += 1

    def calcAdjungateMatrix(self, matrix):
        # Create a matrix of minors
        minors = np.zeros_like(matrix, dtype=int)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                res = int(scipy.linalg.det(minor))
                minors[i, j] = res

        # Create cofactor matrix
        cofactors = np.zeros_like(matrix, dtype=int)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                cofactors[i, j] = (-1) ** (i + j) * minors[i, j]

        # Transpose the cofactor matrix to get the adjugate
        adjugate = cofactors.T
        # print(adjugate)
        return adjugate

    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        detK = int(scipy.linalg.det(np.array(self.keyMatrix))) % 26
        inverseElem = self.findInverseElement(detK) % 26
        adjugateMatrix = self.calcAdjungateMatrix(np.array(self.keyMatrix))
        # print(adjugateMatrix)
        inverseMatrix = inverseElem * adjugateMatrix % 26
        decryptedMessage = ""
        for c in range(len(encryptedMessage)):
            sum = 0
            for c1 in range(len(encryptedMessage)):
                sum += (ord(encryptedMessage[c1]) - ord("a")) * inverseMatrix[c1][c]
            decryptedMessage += chr(sum % 26 + ord("a"))
        return decryptedMessage


def main():
    key = [[3, 25, 4],[23, 6, 15],[13, 17, 21]]
    ha = HillAlgorithm(key)
    encryptedMessage = ha.encryptMessage("you")
    print("Encrypted Message: ", encryptedMessage)
    fullMessage = "ekyimbhkxvnazyuelmvpbjvs"
    fullDecryptedMessage = ""
    for i in range(0, len(fullMessage), 3):
        if(i + 2 < len(fullMessage)):
            encryptedMessage = fullMessage[i:i+3]
        else:
            encryptedMessage = fullMessage[i:]
        decryptedMessage = ha.decryptMessage(encryptedMessage)
        fullDecryptedMessage += decryptedMessage
    print("Decrypted Message: ", fullDecryptedMessage)

if __name__ == '__main__':
    main()