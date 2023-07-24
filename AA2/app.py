from flask import Flask, render_template, request
import os
from hash import generateHash
from time import time
from blockchain import Block, BlockChain

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

chain = BlockChain()

@app.route("/", methods= ["GET", "POST"])
def home():
    print("running")
    print(request.args.get("form"))
    global blockData, encryptedData
    validation = None
    if request.method == "GET":
        return render_template('index.html')
    elif request.args.get("form") == "f1":
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        originalData = { 
                    "sender": sender, 
                    "receiver": receiver, 
                    "amount": amount
                }
        
        sender = generateHash(sender)
        receiver = generateHash(receiver)
        
        transaction = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }
        

        blockData = {
                'index': 1,
                'timestamp': time(),
                'transaction': transaction,
                'previousHash': "No Previous Hash Present. Since this is the first block.",
        }
        newBlock = Block(
                        blockData["index"], 
                        blockData["timestamp"], 
                        blockData["transaction"],
                        blockData["previousHash"])
        chain.addBlock(newBlock)
    
    return render_template('index.html', originalData=originalData, blockData = chain.chain, len=len(chain.chain))
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)