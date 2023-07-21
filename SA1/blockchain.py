from hash import generateHash
import json
from time import time

# Create BlockChain class
class BlockChain:
    # Define __init__() method
    def __init__(self):
        # Create object variable chain and initialize it to an empty list
        self.chain = []

    # Define method createGenesisBlock()    
    def createGenesisBlock(self):
        # Create new object of Block class with index=0, time = time(), empty transaction. In place of hash send string "No Prevoius Hash Present. Since this is the first block." 
        genesisBlock = Block(0, time(), [], "No Previous Hash Present. Since this is the first block.")
        # Append the genesisBlock to the chain
        self.chain.append(genesisBlock)

    # Define printChain method
    def printChain(self):
        # Loop through each block in self.chain and print its data
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transaction", block.transaction)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print("*" * 100 , "\n")

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
    

# Create a new chain using BlockChain class
chain = BlockChain()

# Call createGenesisBlock() method
chain.createGenesisBlock()

# Call printChain() method
chain.printChain()