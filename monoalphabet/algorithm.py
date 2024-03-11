from base_algorithm import Algorithm
import random

class MonoalphabetAlgorithm(Algorithm):

    def __init__(self):
        super().__init__()
        self.alphabet = [chr(elem) for elem in range(ord('a'), ord('z') + 1)]
        self.frequency = self.getFrequencyDictionary()
        self.emptyFrequency = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
        self.emptyFrequency[" "] = 0

    def getFrequencyDictionary(self):
        return {
            "a": 8.167,
            "b": 1.492,
            "c": 2.782,
            "d": 4.253,
            "e": 12.702,
            "f": 2.228,
            "g": 2.015,
            "h": 6.094,
            "i": 6.996,
            "j": 0.153,
            "k": 0.772,
            "l": 4.025,
            "m": 2.406,
            "n": 6.749,
            "o": 7.507,
            "p": 1.929,
            "q": 0.095,
            "r": 5.987,
            "s": 6.327,
            "t": 9.056,
            "u": 2.758,
            "v": 0.978,
            "w": 2.360,
            "x": 0.150,
            "y": 1.974,
            "z": 0.074
        }

    def shuffleAlphabet(self):
        random.shuffle(self.alphabet)

    def encryptMessage(self, originalMessage):
        super().encryptMessage(originalMessage)
        self.shuffleAlphabet()
        encryptedMessage = [self.alphabet[ord(ch) - ord("a")] if ch != " " else " " for ch in originalMessage]
        print("".join(encryptedMessage))
        return "".join(encryptedMessage)

    def calculateFrequencies(self, encryptedMessage):
        for ch in encryptedMessage:
            self.emptyFrequency[ch] += 1
        self.emptyFrequency = {key: value / len(encryptedMessage) for key, value in self.emptyFrequency.items()}

    def findTwoKeysWithBiggestFrequency(self, dict):
        biggest = 0
        bKey = ""
        for ch in dict:
            if dict[ch] > biggest:
                biggest = dict[ch]
                bKey = ch
        secondBiggest = 0
        sbKey = ""
        for ch in dict:
            if dict[ch] > secondBiggest and ch != bKey:
                secondBiggest = dict[ch]
                sbKey = ch
        return bKey, sbKey

    def decryptMessage(self, encryptedMessage):
        encryptedMessage = encryptedMessage.lower()
        super().decryptMessage(encryptedMessage)
        self.calculateFrequencies(encryptedMessage)
        first, second = self.findTwoKeysWithBiggestFrequency(self.emptyFrequency)
        fPredefined, sPredefined = self.findTwoKeysWithBiggestFrequency(self.frequency)
        print(f"We assume that we are mapping {first}->{fPredefined} and {second}->{sPredefined}.")
        print("Rest of decryption we have to continue manually.")
        with open("decrypt-output.txt", "w") as file:
            file.write("Original frequencies in english language {}\n".format(self.frequency))
            file.write("Frequencies from the input text {}\n".format(self.frequency))
            file.write(f"Currently mapped {first}->{fPredefined} and {second}->{sPredefined}\n")

def main():
    ma = MonoalphabetAlgorithm()
    encryptedMessage = ma.encryptMessage("napad je u podne")
    with open("decrypt-input.txt", "r") as file:
        fileDecryptedText = file.readline().strip()
    ma.decryptMessage(fileDecryptedText)

if __name__ == "__main__":
    main()