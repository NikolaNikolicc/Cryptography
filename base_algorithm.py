from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def encryptMessage(self, originalMessage):
        print("---------------------------")
        print("####### ENCRYPTION ########")
        print("---------------------------")

    @abstractmethod
    def decryptMessage(self, encryptedMessage):
        print("---------------------------")
        print("####### DECRYPTION ########")
        print("---------------------------")
