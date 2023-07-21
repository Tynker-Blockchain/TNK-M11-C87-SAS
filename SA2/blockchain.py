
from hash import generateHash
import json
from time import time

class BlockChain:
    def __init__(self):
        self.chain = []

    def createGenesisBlock(self):
        genesisBlock = Block(0, time(), [], "No Previous Hash Present. Since this is the first block.")
        self.chain.append(genesisBlock)

    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transaction", block.transaction)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print("*" * 100 , "\n")
    
    # Define addBlock() method that takes newBlock as parameter 
    def addBlock(self, newBlock):
        # Check if length of the chain is 0 
        if(len(self.chain) == 0):
            # Call createGenesisBlock() method
            self.createGenesisBlock()
        # Get the currentHash of the last block of the chain and use it as previousHash in newBlock    
        newBlock.previousHash = self.chain[-1].currentHash
        # Call calculateHash() method from newBlock and save the hash in currentHash of the newBlock    
        newBlock.currentHash = newBlock.calculateHash()
        # Append the newBlock to the chain
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

sender = "Mike"
receiver = "Sam"
sender = generateHash(sender)
receiver = generateHash(receiver)

transaction = { 
        "sender": sender, 
        "receiver": receiver, 
        "amount": 1000
    }

blockData = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }

newBlock = Block(blockData["index"], 
                 blockData["timestamp"], 
                 blockData["transaction"], 
                 blockData['previousHash'])

chain = BlockChain()

# Replace creation of genesis block with adding newBlock in the blockchain
#chain.createGenesisBlock()
chain.addBlock(newBlock)


chain.printChain()