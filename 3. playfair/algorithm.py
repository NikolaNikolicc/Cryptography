from base_algorithm import Algorithm

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

def getPosition(matrix, letter):
    for r in range(len(matrix)):
        row = matrix[r]
        for e in range(len(row)):
            elem = row[e]
            if elem == letter:
                return Position(e,r)

def sameCol(pos1: Position, pos2: Position) -> bool:
    return pos1.x == pos2.x

def sameRow(pos1: Position, pos2: Position) -> bool:
    return pos1.y == pos2.y

class PlayfairAlgorithm(Algorithm):

    def __init__(self, key):
        self.key = key
        self.matrix = []
        self.rows = self.cols = 5
        self.generateMatrix()

    def printMatrix(self):
        for row in self.matrix:
            print("".join(row))

    '''filter key removes duplicates from key and remove char 'j' from key'''
    def filterKey(self):
        newKey = []
        for ch in self.key:
            if (ch == "j"):
                ch = "i"
            if ch not in newKey:
                newKey.append(ch)
        self.key = newKey
    def generateMatrix(self):
        self.filterKey()
        cnt = 0
        lst = []
        for ch in self.key:
            if(cnt == 0 or cnt % 5 != 0):
                lst.append(ch)
            else:
                self.matrix.append(lst)
                lst = []
                lst.append(ch)
            cnt += 1
        for ch in range(ord("a"), ord("z") + 1):
            if(chr(ch) == "j"): continue
            if(chr(ch) not in self.key):
                if (cnt != 0 and cnt % 5 != 0):
                    lst.append(chr(ch))
                else:
                    self.matrix.append(lst)
                    lst = []
                    lst.append(chr(ch))
                cnt += 1
        self.matrix.append(lst)

    '''preparing message for 3. playfair algorithm (pairs of letters are generated)'''
    def prepareMessage(self, message):
        message = "".join([ch if ch != " " else "" for ch in message])
        changed = True
        while(changed):
            newMessage = ""
            changed = False
            for i in range(0,len(message),2):
                newMessage += message[i]
                if(message[i] == message[i+1]):
                    newMessage += "x"
                    newMessage += message[i + 1:]
                    message = newMessage
                    changed = True
                    break
                newMessage += message[i+1]
        if(len(newMessage) % 2 == 1):
            newMessage += "x"
        # print(newMessage)
        return newMessage

    def getListFromPreparedMessage(self, preparedMessage):
        final = []
        lst = []
        for c in range(len(preparedMessage)):
            if c != 0 and c % 2 == 0:
                final.append(lst)
                lst = []
            lst.append(preparedMessage[c])
        final.append(lst)
        return final
    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        preparedMessasge = self.prepareMessage(originalMessage)
        pairs = self.getListFromPreparedMessage(preparedMessasge)
        # print(pairs)
        encryptedMessage = ""
        for pair in pairs:
            first, second = pair
            firstPos = getPosition(self.matrix, first)
            secondPos = getPosition(self.matrix, second)
            if(sameRow(firstPos, secondPos)):
                encryptedMessage += self.matrix[firstPos.y][(firstPos.x + 1) % len(self.matrix[0])]
                encryptedMessage += self.matrix[secondPos.y][(secondPos.x + 1) % len(self.matrix[0])]
            elif(sameCol(firstPos, secondPos)):
                encryptedMessage += self.matrix[(firstPos.y + 1) % len(self.matrix)][firstPos.x]
                encryptedMessage += self.matrix[(secondPos.y + 1) % len(self.matrix)][secondPos.x]
            else:
                encryptedMessage += self.matrix[firstPos.y][secondPos.x]
                encryptedMessage += self.matrix[secondPos.y][firstPos.x]
            # print(f"{first}: {firstPos}, {second}: {secondPos}")
        # print(encryptedMessage)
        return encryptedMessage

    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        pairs = self.getListFromPreparedMessage(encryptedMessage)
        # print(pairs)
        decryptedMessage = ""
        for pair in pairs:
            first, second = pair
            firstPos = getPosition(self.matrix, first)
            secondPos = getPosition(self.matrix, second)
            if (sameRow(firstPos, secondPos)):
                decryptedMessage += self.matrix[firstPos.y][(firstPos.x - 1) % len(self.matrix[0])]
                decryptedMessage += self.matrix[secondPos.y][(secondPos.x - 1) % len(self.matrix[0])]
            elif (sameCol(firstPos, secondPos)):
                decryptedMessage += self.matrix[(firstPos.y - 1) % len(self.matrix)][firstPos.x]
                decryptedMessage += self.matrix[(secondPos.y - 1) % len(self.matrix)][secondPos.x]
            else:
                decryptedMessage += self.matrix[firstPos.y][secondPos.x]
                decryptedMessage += self.matrix[secondPos.y][firstPos.x]
            # print(f"{first}: {firstPos}, {second}: {secondPos}")
        # print(decryptedMessage)
        return decryptedMessage

def main():
    pfa = PlayfairAlgorithm("vetrobran")
    pfa.printMatrix()
    encyptedMessage = pfa.encryptMessage("napadamo u podne ako ne bude vetra")
    print(f"Encrypted message: {encyptedMessage}")
    decryptedMessage = pfa.decryptMessage(encyptedMessage)
    print(f"Decrypted message: {decryptedMessage}")

if __name__ == '__main__':
    main()