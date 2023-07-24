
from hash import generateHash
import json
from time import time

class BlockChain:
    def __init__(self):
        self.chain = []

    def createGenesisBlock(self):
        # Use Genesis class to create genesis block
        #genesisBlock = Block(0, time(), [], "No Previous Hash Present. Since this is the first block.")
        genesisBlock = Genesis()
        self.chain.append(genesisBlock)

    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transaction", block.transaction)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print("*" * 100 , "\n")
    
    def addBlock(self, newBlock):
        if(len(self.chain) == 0):
            self.createGenesisBlock()
            newBlock.index = 1
        newBlock.previousHash = self.chain[-1].currentHash
        newBlock.currentHash = newBlock.calculateHash()
        self.chain.append(newBlock)

class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()

    def calculateHash(self):
        blockString = str(self.index) + str(self.timestamp) + str(self.previousHash) + str(self.transaction)
        return generateHash(blockString)

# Create a seperate class Genesis for creating genesis block
class Genesis:
    # Define __init__ method
    def __init__(self):
        # Set index, transaction, timestamp, previousHash and currentHash object variables
        self.index = 0
        self.transaction = []
        self.timestamp = time()
        self.previousHash = "No Previous Hash Present. Since this is the first block."
        self.currentHash = ""

