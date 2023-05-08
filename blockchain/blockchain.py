import hashlib
import datetime as dt

class Block:
    def __init__(self, data, previous_block=None):
        self.timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data = data
        self.previous_block = previous_block
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_block).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

class Chain:
    def __init__(self, difficulty=1):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block("Genesis Block")

    def add_block(self, data):
        new_block = Block(data, self.get_last_block().hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def get_last_block(self):
        return self.chain[-1]

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calc_hash():
                return False
            if current_block.previous_block != previous_block.hash:
                return False
        return True
