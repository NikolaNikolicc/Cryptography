from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def encryptMessage(self, originalMessage):
        pass

    @abstractmethod
    def decryptMessage(self, encryptedMessage):
        pass
