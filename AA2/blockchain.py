
from hash import generateHash
import json
from time import time

class BlockChain:
    def __init__(self):
        self.chain = []

    def createGenesisBlock(self):
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

class Genesis:
    def __init__(self):
        self.index = 0
        self.transaction = []
        self.timestamp = time()
        self.previousHash = "No Previous Hash Present. Since this is the first block."
        # Use calculatehash() method to get the currentHash
        self.currentHash = self.calculateHash()

    # define calculateHash() methoddef calculateHash(self):
    def calculateHash(self):
        # Create blockString variable by concatinating index, timestamp, previousHash as string
        blockString = str(self.index) + str(self.timestamp) + str(self.previousHash)
        # Generate the hash using generateHash() function and pass blockstring to it, and the return the result
        return generateHash(blockString)


