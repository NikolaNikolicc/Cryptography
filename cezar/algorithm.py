from base_algorithm import Algorithm
class CesarsAlgorithm(Algorithm):
    def __init__(self, step):
        super().__init__()
        self.step = step
        self.alphabet = [chr(elem) for elem in range(ord('a'), ord('z') + 1)]
    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        message = originalMessage.lower()
        encryptedMessage = [self.alphabet[(ord(ch) - ord('a') + self.step) % len(self.alphabet)] if ch != " " else " " for ch in message]
        print("".join(encryptedMessage).upper())
        return "".join(encryptedMessage).upper()

    def decryptMessage(self, encryptedMessage):
        super().decryptMessage(encryptedMessage)
        message = encryptedMessage.lower()
        originalMessage = [self.alphabet[(ord(ch) - ord('a') - self.step) % len(self.alphabet)] if ch != " " else " " for ch in message]
        print("".join(originalMessage))
        return "".join(originalMessage)

    def bruteForce(self, encryptedMessage):
        print("---------------------------")
        print("####### BRUTE FORCE #######")
        print("---------------------------")
        message = encryptedMessage.lower()
        for step in range(ord("b") - ord("a"), ord("z") - ord("a") + 1):
            possibleMessage = [self.alphabet[(ord(ch) - ord("a") - step) % len(self.alphabet)] if ch != " " else " " for ch in message]
            print("".join(possibleMessage))
def main():
    ca = CesarsAlgorithm(step=3)
    encryptedMessage = ca.encryptMessage("danas duva jak vetar")
    decryptedMessage = ca.decryptMessage(encryptedMessage)
    ca.bruteForce(encryptedMessage)

if __name__ == "__main__":
    main()